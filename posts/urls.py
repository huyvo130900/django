from django.urls import path
from . import views
from .views import login_view, register_view, chatbox_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.post_list, name="posts"),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('chatbox/', chatbox_view, name='chatbox'),  # Chatbox sẽ là "posts/chatbox/"
    path("logout/", auth_views.LogoutView.as_view(next_page='posts'), name="logout"),
    path('posts/<slug:slug>/', views.post_page, name="page"),  
]
