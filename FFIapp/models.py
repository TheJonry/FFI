from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(name="age", null="yes", blank="yes")
    role = models.CharField(name="role", null="yes", blank="yes", max_length=20)

class newsPost(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, related_name="posts", null="True")
    created_at = models.DateTimeField(auto_now_add="True")
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=5000)

    class Meta:
        ordering = ('-created_at',)