from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Permission(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


class User(AbstractUser):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.first_name + " " + self.last_name