from django.test import TestCase, Client
from django.urls import reverse
from .models import OfficerLogin

class OfficerLoginTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('officer_login')
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = OfficerLogin.objects.create(username=self.username, password=self.password)

    def test_get_login_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'officer_login.html')

    def test_valid_login(self):
        form_data = {'username': self.username, 'password': self.password}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirects to another page on successful login

    def test_invalid_login(self):
        form_data = {'username': 'invalid_username', 'password': 'invalid_password'}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid username or password')

    def test_invalid_form_data(self):
        form_data = {'username': '', 'password': ''}
        response = self.client.post(self.url, data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Invalid form data')
