from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Post
from .forms import CustomUserCreationForm, LoginForm

def homepage(request):
    return render(request, "home.html")

def aboutpage(request):
    return render(request, "about.html")

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect("home")
    else:
        form = CustomUserCreationForm()

    return render(request, "posts/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_staff:  # Kiểm tra nếu là admin
                    return redirect('/admin/')
                return redirect("home")  
    else:
        form = LoginForm()

    return render(request, "posts/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

def chatbox_view(request):
    return render(request, "chatbox.html")  

def post_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/post_list.html', {'posts': posts, 'user': request.user})

def post_page(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_page.html', {'post': post})
