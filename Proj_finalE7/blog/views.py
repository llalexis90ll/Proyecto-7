from http.client import HTTPResponse
from django.shortcuts import render , HttpResponse # el http no hay q usar

# Create your views here.
def mi_vista(request):
    return HttpResponse("<h1>IVAN XD</h1><h2>HOLAAaa</h2> ")

#pruebas con html url /documento
def documento (request):
    documento = """
    <html>
    <body>
    <h1>
    DOCUMENTO PRIMERA PAGINA 
    </h1>
    <h2>
    Pruebas de html
    </h2>
    </body>
    </html>

    """ 
    return HttpResponse(documento)