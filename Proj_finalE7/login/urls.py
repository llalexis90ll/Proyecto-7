from django.urls import path
from .views import RegistroUser



urlpatterns = [
    path('registro/',RegistroUser.as_view(), name= 'registro'),


]
