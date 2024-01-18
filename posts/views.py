from django.shortcuts import render, redirect
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

def description(request, slug=None):
    description = Posts.objects.get(id = slug)
    return render(request, 'posts/post_desc.html', {'description': description})