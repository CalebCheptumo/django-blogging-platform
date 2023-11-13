from django.urls import path
from .views import blog_post



urlpatterns = [
    path('posts/', blog_post, name='blog_posts'),
]