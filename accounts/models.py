from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.


def path_and_rename(instance, filename):
    upload_to = "Images/"
    ext = filename.split('.')[-1]

    if instance.username:
        filename = f"User_profile_Pictures/{instance.username}/{instance.username}.{ext}"
    return os.path.join(upload_to, filename)


class CustomUser(AbstractUser):
    address = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=20, blank=False)
    photo = models.ImageField(
        upload_to=path_and_rename, verbose_name="Profile Pic", blank=True)
    

    
    
