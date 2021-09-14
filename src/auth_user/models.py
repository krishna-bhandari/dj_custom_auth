from django.db import models
from django.contrib.auth.models import AbstractUser,ContentType


class User(AbstractUser):
    user_type = models.CharField(max_length=200,null=True,blank=True)
    pass


class CustomUserPermission(models.Model):
    user_type = models.CharField(max_length=200,unique=True)
    content_type = models.ManyToManyField(ContentType)
