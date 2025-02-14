from django.db import models
from django.contrib.auth.models import User

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Story(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cover_image = models.ImageField(upload_to='story_covers/', blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name="stories")  # Many-to-Many Relationship

    def __str__(self):
        return self.title
