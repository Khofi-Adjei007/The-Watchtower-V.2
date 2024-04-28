from django.db import models
from django.core.exceptions import ValidationError


# Registration Model
class new_officer_registrations(models.Model):
    first_name = models.CharField(max_length=250, default='')
    middle_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, default='')
    email = models.CharField(max_length=250)
    phone_contact = models.IntegerField()
    officer_address = models.CharField(max_length=250)
    officer_current_rank = models.CharField(max_length=250)
    officer_current_station = models.CharField(max_length=250)
    officer_staff_ID = models.CharField(max_length=250)
    officer_qualification = models.CharField(max_length=250)
    officer_date_of_birth = models.DateField()
    officer_place_of_operations = models.CharField(max_length=250)
    officer_department_of_operations = models.CharField(max_length=250)
    officer_image = models.ImageField(upload_to='')
    password = models.CharField(max_length=250, default='')


class officer_login(models.Model):
    officer_staff_ID = models.CharField(max_length=250)
    password = models.CharField(max_length=10, default='')