from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Book(models.Model):
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    published = models.IntegerField()