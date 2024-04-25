if request.method == 'POST':
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_contact = request.POST.get('contact')
        officer_address = request.POST.get('address')
        officer_cuurent_rank = request.POST.get('officer_rank')
        officer_current_station = request.POST.get('officer_current_station')
        officer_staff_ID = request.POST.get('officer_staff_ID')
        officer_qualification = request.POST.get('officer_qualification')
        officer_dateofbirth = request.POST.get('officer_qualification')
        officer_place_of_operations = request.POST.get('officer_place_of_operations')
        officer_department_of_operations = request.POST.get('officer_department_of_operations')
        officer_image = request.FILES.get('officer_image')
        password = request.POST.get('password')
        password_two = request.POST.get('password_two')



        # Check if any of the fields are empty
        if not all([first_name, middle_name,last_name,email,phone_contact,officer_address,officer_cuurent_rank, officer_current_station,officer_staff_ID,officer_qualification,
                    officer_dateofbirth,officer_place_of_operations,officer_department_of_operations,officer_image, password, password_two]):
            empty_field_error = 'All fields must be filled.'
            return render(request, 'officer_registrations.html', {'empty_field_error': empty_field_error})
        
          # Check if passwords match
        if password != password_two:
            password_mismatch_error = 'Passwords do not match.'
            return render(request, 'officer_registrations', {'password_mismatch_error': password_mismatch_error})

        # Create user if all checks pass
        User.objects.create_user(first_name=first_name, middle_name=middle_name, password=password)
        messages.success(request, 'Account created successfully!')
        return redirect('officer_account_page')  # Redirect to a success page

    # If GET request or form submission failed, render the form page