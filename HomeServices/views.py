from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import NewOfficerRegistration,OfficerLogin
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .officerRegistrationsForms import officerRegistrationsForms, officer_loginForms
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
import logging





# officer Registrations Views
def redirect_with_delay(request, url, delay_seconds=3):
    return render(request, 'redirect_with_delay.html', {'url': url, 'delay_seconds': delay_seconds})

def officer_registrations(request):
    if request.method == "POST":
        form = officerRegistrationsForms(request.POST, request.FILES)
        if form.is_valid():
            # Extract form data
            officer_first_name = form.cleaned_data['first_name']
            officer_middle_name = form.cleaned_data['middle_name']
            officer_last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            officer_gender = form.cleaned_data['officer_gender']
            officer_email = form.cleaned_data['email']
            officer_phone_contact = form.cleaned_data['phone_contact']
            officer_address = form.cleaned_data['officer_address']
            officer_staff_ID = form.cleaned_data['officer_staff_ID']
            officer_qualification = form.cleaned_data['officer_qualification']
            officer_date_of_birth = form.cleaned_data['officer_date_of_birth']
            officer_operations_region = form.cleaned_data['officer_operations_region']
            officer_current_rank = form.cleaned_data['officer_current_rank']
            officer_current_station = form.cleaned_data['officer_current_station']
            officer_operations_department = form.cleaned_data['officer_operations_department']
            officer_profile_image = form.cleaned_data['officer_profile_image']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)

            # Save data to NewOfficerRegistration table
            User = NewOfficerRegistration.objects.create(
                first_name=officer_first_name,
                middle_name=officer_middle_name,
                last_name=officer_last_name,
                username = username,
                officer_gender = officer_gender,
                email=officer_email,
                phone_contact=officer_phone_contact,
                officer_address=officer_address,
                officer_staff_ID=officer_staff_ID,
                officer_qualification=officer_qualification,
                officer_date_of_birth=officer_date_of_birth,
                officer_operations_region=officer_operations_region,
                officer_current_rank=officer_current_rank,
                officer_current_station=officer_current_station,
                officer_operations_department=officer_operations_department,
                officer_profile_image=officer_profile_image,
                password=hashed_password
            ) 
            User.save()

            # Save Officer_Staff_ID and Password to OfficerLogin table
            OfficerLogin.objects.create(
                password=hashed_password,
                username = username,
            )
            User.objects.create(
                password=hashed_password,
                username = username,
            )

            # Display success message
            messages.success(request, 'Registration successful!')

            # Redirect to officer login page after a short delay (e.g., 2 seconds)
            return redirect_with_delay(request, reverse('officer_login'), delay_seconds=2)
    else:
        form = officerRegistrationsForms()
    return render(request, 'officer_registrations.html', {"form": form})





from django.contrib import messages

def officer_login(request):
    error_message = ''
    
    if request.method == 'POST':
        form = officer_loginForms(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            print(f"Username: {username}, Password: {password}")  # Add this line for debugging
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            print(f"User object: {user}")
            if user is not None:
                login(request, user)
                
                # Redirect to the desired page
                return redirect('officer_account_page')
            else:
                error_message = 'Invalid username or password'
                print("Authentication failed")  # Add this line for debugging
        else:
            # Form is invalid
            error_message = 'Invalid form data'
            print("Form is invalid")  # Add this line for debugging
    else:
        form = officer_loginForms()
        
    return render(request, 'officer_login.html', {'form': form, 'error_message': error_message})


# common context
def get_common_context():
    # Retrieve all common data that needs to be passed to multiple templates
    officer_current_station = " Station Name"  # Example value, replace with actual value

    # Create a context dictionary with all common variables
    common_context = {
        'officer_current_station': officer_current_station,
       
    }
    return common_context

def my_common_context(request):
    # Get common context
    common_context = get_common_context()

    # Add view-specific context
    additional_context = {
        # Add view-specific variables here
    }

    # Merge common context with view-specific context
    context = {**common_context, **additional_context}

    return render(request, 'officer_account_page.html', context)




def submissionpdf(request):
    # To Process Case Input
    pass


# Cookings for the main page
def officer_account_page(request):
    return render(request, 'officer_account_page.html')

