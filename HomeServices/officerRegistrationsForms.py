from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re



# Forms and Authentications goes here
class officerRegistrationsForms(forms.Form):
    first_name = forms.CharField(label="Enter first Name", max_length=100,
                                 error_messages={'required': 'First Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError(_("First name cannot be empty."))
        elif not re.match(r'^[a-zA-Z]*$', first_name):
            raise forms.ValidationError(_("Enter a valid first name."))
        return first_name
    

    middle_name = forms.CharField(max_length=250)
    def clean_middle_name(self):
        middle_name = self.cleaned_data.get('middle_name')
        if middle_name and not re.match(r'^[a-zA-Z]*$', middle_name):
            raise forms.ValidationError(_("Enter a valid middle name."))
        return middle_name
    
    last_name = forms.CharField(max_length=250)
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not re.match(r'^[a-zA-Z]*$', last_name):
            raise forms.ValidationError(_("Enter a valid last name."))
        return last_name
    
    email = forms.CharField(max_length=14)

    phone_contact = forms.CharField()
    def clean_phone_contact(self):
        phone_contact = self.cleaned_data.get('phone_contact')
        if not re.match(r'^\+?1?\d{9,15}$', phone_contact):
            raise forms.ValidationError(_("Enter a valid phone number."))
        return phone_contact

    officer_address = forms.CharField(max_length=250)
    officer_cuurent_rank = forms.CharField(max_length=24)
    officer_current_station = forms.CharField(max_length=24)

    officer_staff_ID = forms.CharField(max_length=12)
    def clean_officer_staff_ID(self):
        officer_staff_ID = self.cleaned_data.get('officer_staff_ID')
        if not re.match(r'^[a-zA-Z0-9]*$', officer_staff_ID):
            raise forms.ValidationError(_("Enter a valid staff ID."))
        return officer_staff_ID
    
    officer_qualification = forms.CharField(max_length=9)
    officer_dateofbirth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    officer_place_of_operations = forms.CharField(label="Officer Operations Area", max_length=24)
    officer_department_of_operations = forms.CharField(max_length=16)
    officer_image = forms.ImageField()
    
    password = forms.CharField(max_length=10, widget=forms.PasswordInput)
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError(_("Password must be at least 8 characters long."))
        return password


    password_two = forms.CharField(max_length=10, widget=forms.PasswordInput)
    def clean_password_two(self):
        password = self.cleaned_data.get('password')
        password_two = self.cleaned_data.get('password_two')
        if password and password_two and password != password_two:
            raise forms.ValidationError(_("The passwords do not match."))
        return password_two


class officer_loginForms(forms.Form):
    user_name = forms.CharField(label="Enter Username (Staff_ID)",max_length=16)
    password = forms.CharField(label="Enter Password",max_length=12)
    pass