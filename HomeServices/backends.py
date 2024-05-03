from django.contrib.auth.backends import BaseBackend
from .models import NewOfficerRegistration # Import your user model

class StaffIDBackend(BaseBackend):
    def authenticate(self, request, officer_staff_ID=None, password=None):
        try:
            user = NewOfficerRegistration.objects.get(officer_staff_ID=officer_staff_ID)
            if user.check_password(password):
                return user
        except NewOfficerRegistration.DoesNotExist:
            return None
