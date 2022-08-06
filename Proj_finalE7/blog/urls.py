from django.urls import path
from .views import Inicio , ArticuloDetalle
#from . import views

urlpatterns = [
    #path('', views.mi_vista, name='mi_vista'),
    #path('documentos',views.documento, name='documento')
    path('', Inicio.as_view(), name='Inicio'),
    path('Post/<int:pk>',ArticuloDetalle.as_view(), name='articulo-detalle'),
]