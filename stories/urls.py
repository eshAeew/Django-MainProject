from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from .views import search_genres

urlpatterns = [
    path('', views.welcome_page, name='welcome_page'),
    path('story_list/', views.story_list, name='story_list'),
    path('story/<int:pk>/', views.story_detail, name='story_detail'),
    path('create/', views.create_story, name='create_story'),
    path('story/<int:pk>/edit/', views.edit_story, name='edit_story'),
    path('story/<int:pk>/delete/', views.delete_story, name='delete_story'),
    path('search-genres/', search_genres, name='search-genres'),
    path('unpublished-stories/', views.unpublished_stories, name='unpublished_stories'),
]



