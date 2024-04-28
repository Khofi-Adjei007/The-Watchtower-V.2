from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .officerRegistrationsForms import officerRegistrationsForms
from .models import new_officer_registrations

class OfficerRegistrationsViewTestCase(TestCase):
    def test_officer_registrations_post(self):
        # Create a POST request
        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            # Add other required form fields
        }
        response = self.client.post(reverse('officer_registrations'), data)
        
        # Check that the response is a redirect
        self.assertEqual(response.status_code, 302)
        
        # Check that a new officer object is created
        self.assertTrue(new_officer_registrations.objects.exists())
        
        # Check that the user is redirected to the login page
        self.assertRedirects(response, reverse('officer_login'))

    def test_officer_registrations_get(self):
        # Create a GET request
        response = self.client.get(reverse('officer_registrations'))
        
        # Check that the response is successful
        self.assertEqual(response.status_code, 200)
        
        # Check that the correct template is used
        self.assertTemplateUsed(response, 'officer_registrations.html')
        
        # Check that the form is passed to the template context
        self.assertIsInstance(response.context['form'], officerRegistrationsForms)
