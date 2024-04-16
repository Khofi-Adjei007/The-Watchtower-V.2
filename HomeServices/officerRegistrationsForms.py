from django import forms
from django.contrib.auth.forms import UserCreationForm




# Forms and Authentications goes here
class officerRegistrationsForms(forms.Form):
        first_name = forms.CharField(
        error_messages={'required': 'First Name is Required .',
                        'invalid': 'Name is Invalid.'})
   
        last_name = forms.CharField(
        error_messages={
                        'required': 'Last Name is Required',
                        'invalid': 'last name is invalid'})
    
        email = forms.EmailField(
        error_messages = {
                        'required': "email field can not be empty",
                        'invalid': "email does not exist"
        })