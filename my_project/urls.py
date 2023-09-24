# project/urls.py
from django.contrib import admin
from django.urls import path, include
from App import views  # Import your app's views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls')),  # Include your app's URLs
]
