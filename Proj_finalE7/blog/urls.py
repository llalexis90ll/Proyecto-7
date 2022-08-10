from django.urls import path
from .views import Inicio , ArticuloDetalle
#from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    #path('', views.mi_vista, name='mi_vista'),
    #path('documentos',views.documento, name='documento')
    path('', Inicio.as_view(), name='Inicio'),
    path('Post/<int:pk>',ArticuloDetalle.as_view(), name='articulo-detalle'),
]

urlpatterns += staticfiles_urlpatterns()