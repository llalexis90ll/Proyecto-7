from django.urls import path

from . import views

urlpatterns = [
    path('', views.mi_vista, name='mi_vista'),
]