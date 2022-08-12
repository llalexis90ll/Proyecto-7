from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class RegistroUser(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'registration/registro.html'
	succes_url = reverse_lazy('login')