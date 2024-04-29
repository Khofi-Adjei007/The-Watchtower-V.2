from django.contrib.auth.backends import BaseBackend
from .models import new_officer_registrations  # Import your user model

class StaffIDBackend(BaseBackend):
    def authenticate(self, request, officer_staff_ID=None, password=None):
        try:
            user = new_officer_registrations.objects.get(officer_staff_ID=officer_staff_ID)
            if user.check_password(password):
                return user
        except new_officer_registrations.DoesNotExist:
            return None
