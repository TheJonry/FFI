from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import forms

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(name="age", null="yes", blank="yes")
    role = models.CharField(name="role", null="yes", blank="yes", max_length=20)
    first_name = models.CharField(name="first_name", null="no", blank="yes", max_length=50)
    last_name = models.CharField(name="last_name", null="no", blank="yes", max_length=100)

class newsPost(models.Model):
    author = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add="True")
    title = models.CharField(max_length=100)
    message = models.TextField(max_length=50000)

    def __str__(self):
        return self.title + " | " + self.author

class boats(models.Model):
    id = models.BigAutoField(primary_key=True)
    
class customers(models.Model):
    id = models.BigAutoField(primary_key=True)

class employees(models.Model):
    id = models.BigAutoField(primary_key=True)

class services(models.Model):
    id = models.BigAutoField(primary_key=True)

class appointments(models.Model):
    id = models.BigAutoField(primary_key=True)

class marinas(models.Model):
    id = models.BigAutoField(primary_key=True)
