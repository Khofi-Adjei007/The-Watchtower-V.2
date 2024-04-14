from django.contrib import admin

# Register your models here.
from .models import portalUsers
from .models import officer_registrations

admin.site.register(portalUsers)
admin.site.register(officer_registrations)