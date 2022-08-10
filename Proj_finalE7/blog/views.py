from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse # el http no hay q usar


from django.views.generic import ListView, DetailView, TemplateView
from .models import Post

# Create your views here.
#def mi_vista(request):
#    return HttpResponse("<h1>IVAN XD</h1><h2>HOLAAaa</h2> ")

#pruebas con html url /documento

# def documento (request):
#     documento = """
#     <html>
#     <body>
#     <h1>
#     DOCUMENTO PRIMERA PAGINA 
#     </h1>
#     <h2 stylo = "color: red">
#     Pruebas de html
#     </h2>
#     </body>
#     </html>

# def documento (request):
#     documento = """
#     <html>
#     <body>
#     <h1>
#     DOCUMENTO PRIMERA PAGINA 
#     </h1>
#     <h2>
#     Pruebas de html
#     </h2>
#     </body>
#     </html>
# >>>>>>> 025b6aba83884c178f7d4563a1675850a7d4c8ed

# #     """ 
# #     return HttpResponse(documento)


class Inicio(ListView):
    model = Post
    template_name = 'inicio.html'


class ArticuloDetalle(DetailView):
    model = Post
    template_name = 'articulo_detalle.html'

