from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class patient(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    username = models.CharField(max_length=50,null=True,unique=True)
    email = models.EmailField(max_length=300)
    address1 = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    pincode = models.IntegerField()
    pic = models.ImageField(upload_to="uploads")

class doctor(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=150)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=300)
    address1 = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    pincode = models.IntegerField()
    pic = models.ImageField(upload_to="uploads")

class contactUs(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.EmailField()
    message = models.TextField()

class blogs(models.Model):
    categories = [
        ('Mental Health','Mental Health'),
        ('Heart Disease','Heart Disease'),
        ('Covid19','Covid19'),
        ('Immunization','Immunization'),
        ('Other','Other')
    ]
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads")
    category = models.CharField(max_length=50,choices=categories)
    summary = models.CharField(max_length=250)
    content = HTMLField()

