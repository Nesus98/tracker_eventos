from django import forms
from .models import Candidatura, Evento # <-- Asegúrate de importar Evento

# 1. El NUEVO molde para Eventos
class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'lugar', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'placeholder': 'Ej. Brunch Electronik'}),
            'lugar': forms.TextInput(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'placeholder': 'Ej. Parc del Fòrum'}),
            # Usamos type='date' para que el navegador muestre el calendario interactivo
            'fecha_inicio': forms.DateInput(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'type': 'date'}),
        }

# 2. Tu molde existente de Candidaturas (se queda casi igual)
class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['evento', 'puesto', 'estado', 'notas']
        widgets = {
            'evento': forms.Select(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none'}),
            'puesto': forms.TextInput(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'placeholder': 'Ej. Control de accesos...'}),
            'estado': forms.Select(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none'}),
            'notas': forms.Textarea(attrs={'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none', 'rows': 3}),
        }