from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
