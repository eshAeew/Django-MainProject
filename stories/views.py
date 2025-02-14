from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Story
from .forms import StoryForm
from stories.models import Story
from accounts.models import *
from django.shortcuts import render, redirect
from .models import Story, Genre
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Genre



story = Story.objects.first()  # Get the first story

if story:
    print(story.cover_image.url if story.cover_image else "No cover image found")
else:
    print("No stories found in the database.")





def welcome_page(request):
    stories_for_welcome = Story.objects.all()
    profile_pic = None 
    all_genres = Genre.objects.all()
    if request.user.is_authenticated:
        stories = Story.objects.filter(is_published=True)
        try:
            profile_pic = UserProfile.objects.get(user=request.user)  # Get the profile for logged-in user
        except UserProfile.DoesNotExist:
            profile_pic = None

        return render(request, 'welcome.html', {'stories': stories, 'profile_pic': profile_pic,'genre': all_genres})

    return render(request, 'welcome.html', {'welcome_page_story': stories_for_welcome, 'profile_pic': profile_pic,'genre': all_genres})




# View for listing all published stories (only for logged-in users)
@login_required
def story_list(request):
    stories = Story.objects.filter(is_published=True)
    return render(request, 'stories/story_list.html', {'stories': stories})

# View for displaying a single story
def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'stories/story_detail.html', {'story': story})






# View for editing a story (only if the logged-in user is the author)
@login_required
def edit_story(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if story.author != request.user:
        return redirect('story_list')  # Prevent unauthorized edits

    if request.method == 'POST':
        form = StoryForm(request.POST, request.FILES, instance=story)  # Add request.FILES
        if form.is_valid():
            form.save()
            return redirect('story_detail', pk=story.pk)
    else:
        form = StoryForm(instance=story)

    return render(request, 'stories/edit_story.html', {'form': form, 'story': story})






# View for deleting a story (only if the logged-in user is the author)
@login_required
def delete_story(request, pk):
    story = get_object_or_404(Story, pk=pk)

    if story.author != request.user:
        return redirect('story_list')  # Prevent unauthorized deletions

    if request.method == 'POST':
        story.delete()
        return redirect('story_list')

    return render(request, 'stories/delete_story.html', {'story': story})






def search_genres(request):
    query = request.GET.get('q', '')
    if query:
        genres = Genre.objects.filter(name__icontains=query).values_list('name', flat=True)[:10]  # Return first 10 matches
    else:
        genres = []
    
    return JsonResponse(list(genres), safe=False)











@login_required
def create_story(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        genre_names = request.POST.get("genres", "").split(",")  # Get genres from hidden input
        cover_image = request.FILES.get("cover_image")  # Get uploaded image
        is_published = request.POST.get("is_published") == "on"  # Convert checkbox to boolean

        story = Story.objects.create(
            title=title,
            content=content,
            author=request.user,
            cover_image=cover_image,  # Save the uploaded image
            is_published=is_published
        )

        for name in genre_names:
            if name.strip():
                genre, created = Genre.objects.get_or_create(name=name.strip())
                story.genres.add(genre)

        return redirect("story_list")  # Redirect to story list page

    return render(request, "stories/create_story.html")






@login_required
def unpublished_stories(request):
    stories = Story.objects.filter(author=request.user, is_published=False)  # Fetch only the user's unpublished stories
    return render(request, 'stories/unpublished_stories.html', {'stories': stories})