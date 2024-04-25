from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import officer_registrations,officer_login
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.models import User, auth
import string
from .officerRegistrationsForms import officerRegistrationsForms, officer_loginForms


# Create your views here.
def officer_account_page(request):
    current_datetime = datetime.now()
    return render(request, 'officer_account_page.html', {"value": current_datetime})


# officer Registrations Views
def officer_registrations(request):
       # if this is a POST request we need to process the form data

    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = officerRegistrationsForms(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            officer_first_name = form.cleaned_data['first_name']
            officer_middle_name = form.cleaned_data['middle_name']
            officer_last_name = form.cleaned_data['last_name']
            officer_email = form.cleaned_data['email']
            officer_phone_contact = form.cleaned_data['phone_contact']
            officer_address  = form.cleaned_data['officer_address']
            officer_staff_ID = form.cleaned_data['officer_staff_ID']
            officer_qualification  = form.cleaned_data[' officer_qualification ']
            officer_dateofbirth = form.cleaned_data[' officer_dateofbirth ']
            officer_place_of_operations  = form.cleaned_data[' officer_place_of_operations ']
            officer_image  = form.cleaned_data[' officer_image ']
            officer_password  = form.cleaned_data[' password ']
            

            new_officer = officer_registrations.objects.create(first_name=officer_first_name,middle_name=officer_middle_name,
                                                               officer_last_name=officer_last_name,email=officer_email, phone_contact=officer_phone_contact,
                                                               officer_address=officer_address, officer_staff_ID=officer_staff_ID,
                                                               officer_qualification=officer_qualification, officer_dateofbirth=officer_dateofbirth,
                                                               officer_place_of_operations=officer_place_of_operations,
                                                               officer_image=officer_image,officer_password=officer_password)
            new_officer.save()
            return render(request, 'oofficer_login/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = officerRegistrationsForms()

    return render(request, 'officer_registrations.html', {"form": form})



    # Function to handle logins
def officer_login(request):
    if request.method == 'POST':
        forms = officer_loginForms(request.POST)
        username = request.POST.get('username')
        password = request.POST['password']
        user = authenticate(username=username, password=password)
    
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('officer_login')
        else:
            for field, errors in forms.erros.items():
                for error in errors:
                    messages.error(request, f"{field}:{error}")
            messages.error(request,'username or password not correct')
            return redirect('/')
    
    else:
        forms = officer_loginForms(request)
    return render(request, 'officer_login.html', {'form': forms})


def submissionpdf(request):
    # To Process Case Input
    pass