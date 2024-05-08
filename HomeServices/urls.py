from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('officer_registrations/', views.officer_registrations, name='officer_registrations'),
    path('officer_login/', views.officer_login, name='officer_login'),
    path('officer_account_page/', views.officer_account_page, name='officer_account_page'),
    path('submissionpdf/', views.submissionpdf, name='submissionpdf'),
    path('eagle_eye/', views.eagle_eye, name='eagle_eye'),
    path('officer_logout/', views.officer_logout, name='officer_logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)