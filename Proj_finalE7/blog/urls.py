from django.urls import path
from .views import Inicio , ArticuloDetalle,CrearPost,EditarPost,BorrarPost, Institucional,NuestraHistoria,NovedadesView,Powered
#from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    #path('', views.mi_vista, name='mi_vista'),
    #path('documentos',views.documento, name='documento')
    path('', Inicio.as_view(), name='Inicio'),
    path('Post/<int:pk>',ArticuloDetalle.as_view(), name='articulo-detalle'),
    path('crear_post/', CrearPost.as_view(), name='crear-post'),
    path('Post/edit/<int:pk>',EditarPost.as_view(), name='editar-post'),
    path('Post/<int:pk>/remover',BorrarPost.as_view(), name='borrar-post'),
    path('INSTITUCIONAL',Institucional.as_view(), name='institucional'),
    path('NUESTRA_HISTORIA',NuestraHistoria.as_view(), name='nuestra-historia'),
    path('Novedades/',NovedadesView.as_view(), name='novedades'),
    path('About/',Powered.as_view(), name='powered'),
]

urlpatterns += staticfiles_urlpatterns()