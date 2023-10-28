from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Room(models.Model):
    name=models.CharField(default="",max_length=50)
    slug=models.SlugField(unique=True)
    