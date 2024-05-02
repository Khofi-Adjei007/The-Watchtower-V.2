from django.contrib.auth.backends import BaseBackend
from .models import OfficerLogin

class OfficerAuthBackend(BaseBackend):
    def authenticate(self, request, officer_staff_ID=None, password=None):
        try:
            # Retrieve the user with the provided officer_staff_ID
            officer = OfficerLogin.objects.get(officer_staff_ID=officer_staff_ID)
            # Check if the provided password matches the user's password
            if officer.check_password(password):
                # Return the authenticated user
                return officer
        except OfficerLogin.DoesNotExist:
            # If the user does not exist, return None
            return None
    
    # You may also need to implement the following methods:
    # def get_user(self, user_id):
    #     return OfficerLogin.objects.get(pk=user_id)
