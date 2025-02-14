from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import ProfileUpdateForm
from stories.models import *

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('story_list')  # Redirect to the story list page
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('story_list')  # Redirect to the story list page
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# @login_required
# def profile_view(request):
#     user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = ProfileUpdateForm(instance=user_profile)
    
#     return render(request, 'accounts/profile.html', {'form': form})


@login_required
def profile_view(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=user_profile)

    return render(request, 'accounts/profile.html', {
        'form': form,
        'user_profile': user_profile  # Pass user_profile to the template
    })












