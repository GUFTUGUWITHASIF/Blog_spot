from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='default-slug')


    def __str__(self):
        return self.name
    
   




class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, default='default-slug')


    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)  # Keep only updated_on
    content = models.TextField()
    tags = TaggableManager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', default=1)

    class Meta:
        ordering = ['-updated_on']  # Update ordering to use updated_on

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    # Add more fields as needed

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed
