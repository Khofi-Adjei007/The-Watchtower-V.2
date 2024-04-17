from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import officer_registrations
from django.contrib import messages
from django.contrib.auth.models import User, auth
import string
from django.contrib.auth.models import User
from .officerRegistrationsForms import officerRegistrationsForms


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
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'officer_login.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = officerRegistrationsForms()

    return render(request, 'officer_registrations.html', {"form": form})



def officer_login(request):
    return render(request, 'officer_login.html')


def submissionpdf(request):
    pass