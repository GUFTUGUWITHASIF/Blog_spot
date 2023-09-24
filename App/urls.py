# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, ProfileViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'STATUS', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
