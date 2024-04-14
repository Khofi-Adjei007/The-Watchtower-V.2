from . import views
from django.http import HttpResponse
from django.urls import path


urlpatterns = [
    path('officer_account_page/', views.officer_account_page,),
    path('officer_login/', views.officer_login),
    path('officer_registrations/', views.officer_registrations),
    path('submissionpdf/', views.submissionpdf, name='submissionpdf'),
]