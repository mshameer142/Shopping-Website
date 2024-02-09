from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
import uuid
import sqlite3


# Create your models here.
class Registration(models.Model):
    Password = models.CharField(max_length=200, null=True)
    User_role = models.CharField(max_length=200, null=True)
    user = models.OneToOneField(User,on_delete = models.CASCADE, null = True)

    def __str__(self):
     return self.User_role


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Password = models.CharField(max_length=200, null=True)


class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, default="default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Messages(models.Model):
    Message_content = models.TextField(null=True)
    From_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null=True, related_name='from_message')
    To_reg = models.ForeignKey(Registration, on_delete=models.SET_NULL, null=True, related_name='to_message')


class Guest_messages(models.Model):
    Name = models.CharField(max_length = 200, null=True)
    Email = models.CharField(max_length=200, null=True)
    Message_content = models.TextField(null=True)


class Payment(models.Model):
    CARD_HOLDER = models.CharField(max_length=200, null=True)
    CARD_NUMBER = models.CharField(max_length=200, null=True)
    EXPIRE = models.CharField(max_length=20, null=True)
    CVV = models.CharField(max_length=20, null=True)














