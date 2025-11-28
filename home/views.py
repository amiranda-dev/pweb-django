from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse('<h1>Página Principal</h1>')

def sobre(request):
    return HttpResponse('<h1>Sobre o Sistema Django!</h1>')

def contato(request):
    return HttpResponse('<h1>Contato</h1>')

def ajuda(request):
    return HttpResponse('<h1>Ajuda</h1>')