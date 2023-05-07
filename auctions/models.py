from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200, unique=True)

class AuctionList(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=64,null=False, blank=False)
    description = models.TextField(blank=True)
    current_price = models.IntegerField(null=False, blank=True)
    photo = models.TextField(blank=True)
    categories = models.CharField(max_length=50)

class Comments(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField(blank=True)