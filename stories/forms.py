# from django import forms
# from .models import Story

# class StoryForm(forms.ModelForm):
#     class Meta:
#         model = Story
#         fields = ['title', 'content', 'is_published']  # Add 'is_published' field here

#     # Optional: Add a custom widget to make the checkbox nicer
#     is_published = forms.BooleanField(required=False, label="Publish story immediately")




from django import forms
from .models import *

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content', 'is_published', 'cover_image']  # Include cover image

    cover_image = forms.ImageField(required=False, label="Upload Cover Image")  # Optional image field
