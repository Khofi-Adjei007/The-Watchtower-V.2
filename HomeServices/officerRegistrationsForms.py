from django import forms
from django.db import models
from .models import new_officer_registrations
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re



# Forms and Authentications goes here
class officerRegistrationsForms(forms.Form):

    class Meta:
        model = new_officer_registrations
        fields = '__all__'

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
    

    middle_name = forms.CharField(max_length=250,)
    def clean_middle_name(self):
        middle_name = self.cleaned_data.get('middle_name')
        if middle_name and not re.match(r'^[a-zA-Z]*$', middle_name):
            raise forms.ValidationError(_("Enter a valid middle name."))
        return middle_name
    
    last_name = forms.CharField(label="Enter last Name", max_length=250,
                                error_messages={'required': 'Last Name is Required .',
                                                    'invalid': 'Name is Invalid.'})
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name and not re.match(r'^[a-zA-Z]*$', last_name):
            raise forms.ValidationError(_("Enter a valid last name."))
        return last_name
    
    email = forms.CharField(max_length=250)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError("email must end with @example.com")
        return email

    phone_contact = forms.CharField()
    def clean_phone_contact(self):
        phone_contact = self.cleaned_data.get('phone_contact')
        if not re.match(r'^\+?1?\d{9,15}$', phone_contact):
            raise forms.ValidationError(_("Enter a valid phone number."))
        return phone_contact


    officer_address = forms.CharField(max_length=250,
                                      error_messages={'required': 'Address is Required .',
                                                        'invalid': 'Name is Invalid.'})
    def clean_officer_address(self):
        officer_address = self.cleaned_data.get('officer_address')
        if not officer_address:
            raise forms.ValidationError(_("Address cannot be empty."))
            # Additional validation logic if needed
        return officer_address

    officer_current_rank = forms.CharField(max_length=24)
    officer_current_station = forms.CharField(max_length=24)

    officer_staff_ID = forms.CharField(max_length=12)
    def clean_officer_staff_ID(self):
        officer_staff_ID = self.cleaned_data.get('officer_staff_ID')
        if not re.match(r'^[a-zA-Z0-9]*$', officer_staff_ID):
            raise forms.ValidationError(_("Enter a valid staff ID."))
        return officer_staff_ID
    
    officer_qualification = forms.CharField(max_length=250)
    def clean_officer_qualification(self):
        officer_qualifications = self.cleaned_data.get('officer_qualification')
        if not re.match(r'^[a-zA-Z0-9]*$', officer_qualifications):
            raise forms.ValidationError(_("Enter a valid qualification"))
        return officer_qualifications


    officer_date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    officer_place_of_operations = forms.CharField(label="Area of Operations", max_length=24)
    officer_department_of_operations = forms.CharField(max_length=16)

    officer_image = forms.ImageField()
    def clean_officer_image(self):
        officer_image = self.cleaned_data.get('officer_image')
        if not officer_image:
            raise forms.ValidationError('Image is required')
        return officer_image
    
    password = forms.CharField(label="Enter Password",max_length=250, widget=forms.PasswordInput)
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError(_("Password must be at least 8 characters long."))
        return password


    confirm_password = forms.CharField(label="Confirm Password", max_length=250, widget=forms.PasswordInput)
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(_("The passwords do not match."))
        return confirm_password


class officer_loginForms(forms.Form):
    user_name = forms.CharField(label="Enter Username (Staff_ID)",max_length=16)
    password = forms.CharField(label="Enter Password",max_length=12)
    pass