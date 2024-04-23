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
        form = officerRegistrationsForms(request.POST)

        # check whether it's valid:
        if form.is_valid():
            first_name = form.cleaned_data('first_name')



            officer_staff_ID = form.cleaned_data['officer_staff_ID']
            if len(officer_staff_ID) < 6:
                error_message = "Staff ID must be at least 6 characters long."
                return render(request, 'officerRegistrationsForms.html', {'form': form, 'error_message': error_message})
            
            return render(request, 'officer_login.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = officerRegistrationsForms()

    return render(request, 'officer_registrations.html', {"form": form})



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
    pass