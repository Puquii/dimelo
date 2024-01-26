from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePost
from .models import Posts
# Create your views here.

def index(request):
    discounts = Posts.objects.all().order_by('-created')
    return render(request, 'index.html', {'discounts': discounts})

def submit(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.user = request.user
            user_form.save()
            return redirect('index')
        
    else:
        form = CreatePost()
    return render(request, 'posts/create_post.html', {'form': form})

def edit(request, slug):
    post = get_object_or_404(Posts, slug=slug)
    if request.method == 'POST':
        form = CreatePost(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('userinfo')
    else:
        form = CreatePost(instance=post)
    
    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

def description(request, slug):
    description = Posts.objects.get(slug = slug)
    return render(request, 'posts/post_desc.html', {'description': description})