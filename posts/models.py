from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.text import slugify

class CustomUser(AbstractUser):
    VAI_TRO_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    vai_tro = models.CharField(max_length=10, choices=VAI_TRO_CHOICES, default='user')

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, default="")
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title
