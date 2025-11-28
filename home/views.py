from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse('Hello, World!')


def sobre(request):
    return HttpResponse('Sobre o sistema')