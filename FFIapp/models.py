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

class Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    Title = models.CharField(max_length=50)
    Description = models.TextField(max_length=3000)
    Unit_Price = models.PositiveSmallIntegerField()
    Unit_Price_Description = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class Marina(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Street = models.CharField(max_length=50)
    City = models.CharField(max_length=25)
    Zip = models.PositiveSmallIntegerField()

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)

class Boat(models.Model):
    id = models.BigAutoField(primary_key=True)
    Owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Size = models.PositiveSmallIntegerField()
    Preferred_Interval = models.PositiveSmallIntegerField()

class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Can_Do = models.ManyToManyField(Service) 

class Appointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    Date_Submitted = models.DateField(auto_now_add=True)
    Date_Of_Appointment = models.DateField(auto_now=False, auto_now_add=False)
    Boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    Marina = models.ForeignKey(Marina, on_delete=models.CASCADE)
    Slip = models.CharField(max_length=15)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Clean_Service = models.BooleanField(default=True)
    Zinc_Service = models.BooleanField(default=False)
    Zinc_Service_Units = models.PositiveSmallIntegerField()
    Status = models.TextChoices("Status", "APPLIED CONFIRMED CANCELLED RESCHEDULED COMPLETE")


