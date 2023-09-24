# views.py
from rest_framework import viewsets
from .models import Post, Profile, Comment
from .serializers import PostSerializer, ProfileSerializer, CommentSerializer
from .filters import PostFilter  # Import your custom filter

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filterset_class = PostFilter  # Use the custom filter class


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
