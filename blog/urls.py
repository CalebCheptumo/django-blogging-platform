from django.urls import path
from .views import blog_post , create_blog_post



urlpatterns = [
    path('posts/', blog_post, name='blog_posts'),
    path('create/', create_blog_post, name='create_blog_post'),
]