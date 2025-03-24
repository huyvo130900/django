from django.contrib import admin
from django.urls import path, include
from posts.views import chatbox_view
from . import views
from posts import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),  # Gọi đúng hàm trong views.py
    path('about/', views.aboutpage, name='about'),
    path('chatbox/', chatbox_view, name='chatbox'), 
    path('gioi-thieu/', views.aboutpage),
    path('posts/', include('posts.urls')),
]
