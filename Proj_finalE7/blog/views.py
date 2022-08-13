from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse # el http no hay q usar


from django.views.generic import ListView, DetailView, TemplateView , CreateView , UpdateView, DeleteView
from .models import Post

from .forms import PostForm
from django.urls import reverse_lazy
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
    ordering = ['-created_date']


class ArticuloDetalle(DetailView):
    model = Post
    template_name = 'articulo_detalle.html'

class CrearPost(CreateView):
    model = Post
    form_class = PostForm
    template_name= 'add_post.html'

class EditarPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'

class BorrarPost(DeleteView):
    model = Post
    template_name = 'borrar_post.html'
    success_url = reverse_lazy('Inicio')

class NuestraHistoria(TemplateView):
    template_name = "NUESTRA_HISTORIA.html"