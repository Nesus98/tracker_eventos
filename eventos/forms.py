from django import forms
from .models import Candidatura

class CandidaturaForm(forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['evento', 'puesto', 'estado', 'notas']
        
        # Los 'widgets' controlan cómo se dibuja el HTML de cada campo
        widgets = {
            'evento': forms.Select(attrs={
                'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all'
            }),
            'puesto': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all',
                'placeholder': 'Ej. Control de accesos, Técnico...'
            }),
            'estado': forms.Select(attrs={
                'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all'
            }),
            'notas': forms.Textarea(attrs={
                'class': 'w-full px-4 py-2 mt-1 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition-all',
                'rows': 3,
                'placeholder': 'Opcional: Detalles sobre la oferta...'
            }),
        }