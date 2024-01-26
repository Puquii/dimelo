from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm, LoginForm, PasswordChangeForm
from posts.models import Posts

# Create your views here.


def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, "users/login.html", {'form': form})

@login_required
def changePassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'users/change_password.html', {'form': form})

@login_required
def user_info(request):
    passwordChange = PasswordChangeForm(user=request.user, data = request.POST)
    posts = Posts.objects.all().filter(user = request.user)
    if request.method == 'POST':
        return redirect('post_edit')
    return render(request, 'users/userinfo.html', {'posts': posts, 'passwordChange' : passwordChange})

def user_logout(request):
    logout(request)
    return redirect('index')