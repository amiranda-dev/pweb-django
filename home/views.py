from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def ajuda(request):
    return render(request, 'ajuda.html')

def exibir_item(resquest, id):
    return render(resquest, "exibir_item.html", {'id':id})

def perfil(request, usuario):
    return render(request, "perfil.html", {'usuario':usuario})

def dia_semana(request, numero):
    dias = {
        1: "Segunda-feira",
        2: "Terça-feira",
        3: "Quarta-feira",
        4: "Quinta-feira",
        5: "Sexta-feira",
        6: "Sábado",
        7: "Domingo"
    }
    
    dia = dias.get(numero, "Dia inválido")
    
    return render(request, "dia.html", {"dia":dia})