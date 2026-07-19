from django.urls import path
from .views import loisirs_view


urlpatterns = [
    path('', loisirs_view, name='loisirs'),
]