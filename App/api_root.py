# App/api_root.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

class CustomAPIRoot(APIView):
    def get(self, request, format=None):
        return Response({
            "posts": reverse('post-list', request=request, format=format),
            "profiles": reverse('profile-list', request=request, format=format),
            "comments": reverse('comment-list', request=request, format=format),
        })
