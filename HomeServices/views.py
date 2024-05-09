from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from .models import NewOfficerRegistration,OfficerLogin
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .officerRegistrationsForms import officerRegistrationsForms, officer_loginForms
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect






# officer Registrations Views
def redirect_with_delay(request, url, delay_seconds=3):
    return render(request, 'redirect_with_delay.html', {'url': url, 'delay_seconds': delay_seconds})


# New Officers Registration Views
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
            user, created = User.objects.get_or_create(username=username, email=officer_email)
            if created:
                user.set_password(password)
                user.save()

            new_officer_registration = NewOfficerRegistration.objects.create(
                user=user,
                first_name=officer_first_name,
                middle_name=officer_middle_name,
                last_name=officer_last_name,
                username=username,
                officer_gender=officer_gender,
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
            )

            # Display success message
            messages.success(request, 'Registration successful!')

            # Redirect to officer login page after a short delay (e.g., 2 seconds)
            return redirect_with_delay(request, reverse('officer_login'), delay_seconds=2)
    else:
        form = officerRegistrationsForms()
    return render(request, 'officer_registrations.html', {"form": form})




# officer login views
def officer_login(request):
    error_message = ''
    if request.method == 'POST':
        form = officer_loginForms(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Authenticate user
            user = authenticate(username=username, password=password)
            print(f"User object: {user}")
            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['officer_staff_ID'] = user.newofficerregistration.officer_staff_ID
                request.session['officer_current_rank'] = user.newofficerregistration.officer_current_rank

                # Redirect to the desired page
                return redirect('officer_account_page')
            else:
                error_message = 'Invalid username or password'
        else:
            # Form is invalid
            error_message = 'Invalid form data'
            print("Form is invalid")
    else:
        form = officer_loginForms()
    return render(request, 'officer_login.html', {'form': form, 'error_message': error_message})



# officer logout views
def officer_logout(request):
    logout(request)
    request.session.clear()
    return HttpResponseRedirect(reverse('officer_login'))




# views to handle report case
def submissionpdf(request):
    # Get the content from the POST request
    content = request.POST.get('content', '')

    # Create a PDF document
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="docket.pdf"'

    # Create a ReportLab document
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    style_heading = styles['Heading1']
    style_paragraph = ParagraphStyle(name='Normal', fontName='Helvetica', fontSize=12, leading=14)

    # Add content to the PDF
    paragraphs = []
    paragraphs.append(Paragraph("Docket Content:", style_heading))
    paragraphs.append(Spacer(1, 12))
    paragraphs.append(Paragraph(content, style_paragraph))

    # Build the PDF document
    doc.build(paragraphs)

    return response

# Cookings for the main page
@login_required
def officer_account_page(request):
    return render(request, 'officer_account_page.html')


def eagle_eye(request):
    return render(request, 'eagle_eye.html')