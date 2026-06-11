from django.shortcuts import render
from .models import Evento, Candidatura

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def lista_candidaturas(request):
    candidaturas = Candidatura.objects.all()
    return render(request, 'eventos/lista_candidaturas.html', {'candidaturas': candidaturas})