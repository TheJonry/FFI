from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    age = models.PositiveIntegerField(name="age", null="yes", blank="yes")
    role = models.CharField(name="role", null="yes", blank="yes", max_length=20)