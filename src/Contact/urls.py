from django.contrib import admin
from django.urls import path
from Contact.views import contact_view, privacy_policy



urlpatterns = [
    path('', contact_view, name='contact'),
    path('privacy-policy/', privacy_policy, name='privacy-policy'),
]
