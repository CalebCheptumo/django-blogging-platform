from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def blog_post(request):
    posts =BlogPost.objects.all()
    return render(request,'blog/blog_posts.html',{'posts':posts})
