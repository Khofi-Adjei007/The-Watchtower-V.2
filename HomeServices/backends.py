from django.contrib.auth.backends import ModelBackend
from .models import OfficerLogin

class StaffIDBackend(ModelBackend):
    def authenticate(self, request, staff_ID=None, password=None, **kwargs):
        try:
            # Query the OfficerLogin model directly
            user = OfficerLogin.objects.get(officer_staff_ID=staff_ID)
            if user.check_password(password):
                return user
        except OfficerLogin.DoesNotExist:
            return None

        return None
