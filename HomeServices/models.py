from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class portalUsers(models.Model):
    userName = models.CharField(max_length=100)
    details = models.CharField(max_length=250,default=0)


class officer_registrations(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=14)
    first_name = models.CharField(max_length=250, default='')
    last_name = models.CharField(max_length=250, default='')
    password = models.CharField(max_length=10, default='')
    password_two = models.CharField(max_length=10, default='')


class officer_login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10, default='')