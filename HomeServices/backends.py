from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import NewOfficerRegistration


class StaffIDBackend(BaseBackend):
    def authenticate(self, request, officer_staff_ID=None, password=None):
        try:
            user = NewOfficerRegistration.objects.get(officer_staff_ID=officer_staff_ID)
            if user.check_password(password):
                return user
        except NewOfficerRegistration.DoesNotExist:
            return None
