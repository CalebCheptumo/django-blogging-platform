from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm


@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(blog_post)
    else:
            form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html',{'form' : form})




def blog_post(request):
    posts =BlogPost.objects.all()
    return render(request,'blog/blog_posts.html',{'posts':posts})
