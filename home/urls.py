
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.index, name="index"),
    path('sobre/', views.sobre, name="sobre_sistema"),   
    path('contato/', views.contato, name="contato"),   
    path('ajuda/', views.ajuda, name="ajuda"),
    path('item/<int:id>', views.exibir_item, name="exibir_item")      
]
