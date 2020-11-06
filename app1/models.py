from django.db import models
from django.contrib.auth.models import AbstractUser


class user(AbstractUser):
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=16)