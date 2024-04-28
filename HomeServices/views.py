from django.shortcuts import render, redirect
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import new_officer_registrations,officer_login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from .officerRegistrationsForms import officerRegistrationsForms, officer_loginForms




# officer Registrations Views
def officer_registrations(request):
    if request.method == "POST":
        form = officerRegistrationsForms(request.POST, request.FILES)
        if form.is_valid():
            officer_first_name = form.cleaned_data['first_name']
            officer_middle_name = form.cleaned_data['middle_name']
            officer_last_name = form.cleaned_data['last_name']
            officer_email = form.cleaned_data['email']
            officer_phone_contact = form.cleaned_data['phone_contact']
            officer_address  = form.cleaned_data['officer_address']
            officer_staff_ID = form.cleaned_data['officer_staff_ID']
            officer_qualification  = form.cleaned_data['officer_qualification']
            officer_date_of_birth = form.cleaned_data['officer_date_of_birth']
            officer_place_of_operations  = form.cleaned_data['officer_place_of_operations']
            officer_current_rank  = form.cleaned_data['officer_current_rank']
            officer_current_station  = form.cleaned_data['officer_current_station']
            officer_department_of_operations  = form.cleaned_data['officer_department_of_operations']
            officer_image  = form.cleaned_data['officer_image']
            password  = form.cleaned_data['password']
            

            # Create a new instance of the model
            new_officer = new_officer_registrations.objects.create(
                first_name=officer_first_name,
                middle_name=officer_middle_name,
                last_name=officer_last_name,
                email=officer_email,
                phone_contact=officer_phone_contact,
                officer_address=officer_address,
                officer_staff_ID=officer_staff_ID,
                officer_qualification=officer_qualification,
                officer_date_of_birth=officer_date_of_birth,
                officer_place_of_operations=officer_place_of_operations,
                officer_current_rank=officer_current_rank,
                officer_current_station=officer_current_station,
                officer_department_of_operations=officer_department_of_operations,
                officer_image=officer_image,
                password=password
            )
            # Save the new instance
            new_officer.save()
            return HttpResponseRedirect(reverse('officer_login'))

    else:
        form = officerRegistrationsForms()
    return render(request, 'officer_registrations.html', {"form": form})





# Function to handle logins
def officer_login(request):
    if request.method == 'POST':
        form = officer_loginForms(request.POST)
        if form.is_valid():
            officer_staff_ID = form.cleaned_data['officer_staff_ID']
            password = form.cleaned_data['password']

            # Authenticate user using staff ID
            user = authenticate(request, officer_staff_ID=officer_staff_ID, password=password)
            if user is not None:
                login(request, user)
                
            # Redirect to a officer account_page
            return HttpResponseRedirect(reverse('officer_account_page'))
    
        else:
            # Authentication failed
            error_message = 'Staff ID or password Is Incorrect.'
            return render(request, 'officer_login.html', {'form': form, 'error_message': error_message})
    else:
        form = officer_loginForms()
        return render(request, 'officer_login.html', {'form': form})


def submissionpdf(request):
    # To Process Case Input
    pass


# Cookings for the main page
def officer_account_page(request):
    return render(request, 'officer_account_page.html')
