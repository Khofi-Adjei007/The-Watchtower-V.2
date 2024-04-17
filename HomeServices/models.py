from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class portalUsers(models.Model):
    userName = models.CharField(max_length=100)
    details = models.CharField(max_length=250,default=0)


# Registration Model
class officer_registrations(models.Model):
    first_name = models.CharField(max_length=250, default='')
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, default='')
    email = models.CharField(max_length=14)
    phone_contact = models.IntegerField()
    officer_address = models.CharField(max_length=250)
    officer_cuurent_rank = models.CharField(max_length=24)
    officer_current_station = models.CharField(max_length=24)
    officer_staff_ID = models.CharField(max_length=12)
    officer_qualification = models.CharField(max_length=9)
    officer_date_of_birth = models.DateField()
    officer_place_of_operations = models.CharField(max_length=24)
    officer_department_of_operations = models.CharField(max_length=16)
    officer_image = models.ImageField(upload_to='')
    password_two = models.CharField(max_length=10, default='')


class officer_login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10, default='')