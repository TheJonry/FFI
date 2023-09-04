from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import forms

class UserProfile(AbstractUser):
    role = models.CharField(name="role", null="yes", blank="yes", max_length=20)
    first_name = models.CharField(name="first_name", null="yes", blank="yes", max_length=50)
    last_name = models.CharField(name="last_name", null="yes", blank="yes", max_length=100)

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
    Base_Price = models.PositiveSmallIntegerField(blank=True, null=True)
    Unit_Price = models.PositiveSmallIntegerField(blank=True, null=True)
    Unit_Price_Description = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class Region(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

# class Credentials
    #Advanced diver cert
    #Master diver cert
    #Commercial diver
    #Dive instructor
    #Cave diver
    #CPR
    #Medical certifications
    #Prop changes "SQUID"

class Marina(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    Street = models.CharField(max_length=50, blank=True, null=True)
    City = models.CharField(max_length=25, blank=True, null=True)
    Zip = models.PositiveSmallIntegerField(blank=True, null=True)
    Region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)
    Note = models.TextField(max_length=500, default="No notes.", blank=True, null=True)
    Entry_Instructions = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.Name

class Customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=30, blank=True, null=True)
    Last_Name = models.CharField(max_length=30, blank=True, null=True)
    Street = models.CharField(max_length=50, default="", blank=True, null=True)
    City = models.CharField(max_length=25, default="", blank=True, null=True)
    Zip = models.PositiveSmallIntegerField( blank=True, null=True)
    Note = models.TextField(max_length=500, default="No notes.", blank=True, null=True)
    Contact_Info = models.CharField(max_length=50, default="", blank=True, null=True)

    def __str__(self):
        return self.Last_Name + ", " + self.First_Name

class boat_Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    zinc_Count = models.PositiveSmallIntegerField()
    # Reserach additional boat sales site for details
    # Year
    # Bow Through Holes number and locations
    # Stern Through Holes number and locations
    # Ledges
    # Cleaning Tips
    # Boat Diagram
    # Sea chest opening instructions
    # Other grates covering

class Boat(models.Model):
    id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=50, default="Boat")
    Owner = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True, null=True)
    Size = models.PositiveSmallIntegerField()
    Preferred_Interval = models.PositiveSmallIntegerField()
    # Model char
    # Make char
    # Year
    # Serial Number 
    # Registration Number
    # Engine HP
    # Number of engines
    # Outboard?
    # Aftermarket additions
    # Swim platform
    # Reference photo

    Note = models.TextField(max_length=500, default="No notes.", blank=True, null=True)

    def __str__(self):
        return self.Name



class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    # Credentails
    Note = models.TextField(max_length=500, default="No notes.", blank=True, null=True)
    Status = models.CharField(blank=True, null=True, max_length=30)

    def __str__(self):
        return self.Last_Name + ", " + self.First_Name

class Appointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    Date_Submitted = models.DateField(auto_now_add=True)
    Date_Of_Appointment = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Boat = models.ForeignKey(Boat, on_delete=models.CASCADE)
    Marina = models.ForeignKey(Marina, on_delete=models.CASCADE)
    Slip = models.CharField(max_length=15, blank=True, null=True)
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    Clean_Service = models.BooleanField(default=True)
    Zinc_Service = models.BooleanField(default=False)
    Zinc_Service_Units = models.PositiveSmallIntegerField(blank=True, null=True)
    Status = models.TextChoices("Status", "APPLIED CONFIRMED CANCELLED RESCHEDULED COMPLETE")
    Note = models.TextField(max_length=500, default="No notes.", blank=True, null=True)
    #before photos
    #after photos

    def __str__(self):
        return self.Date_Of_Appointment + " : " + self.Marina + " - " + self.Boat


