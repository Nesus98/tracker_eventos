from django.shortcuts import render, redirect
from .models import Evento
from .forms import CandidaturaForm # <-- Importamos el molde que acabas de crear

def lista_eventos(request):
    # Traemos todos los eventos (igual que antes)
    festivales = Evento.objects.all()
    
    # ¿El usuario acaba de darle al botón de enviar formulario?
    if request.method == 'POST':
        # Rellenamos el molde con los datos que llegaron de la web
        form = CandidaturaForm(request.POST)
        
        # Django verifica automáticamente por seguridad si los datos son correctos
        if form.is_valid():
            form.save() # ¡Se guarda en la base de datos automáticamente!
            return redirect('lista_eventos') # Recargamos la página para ver el nuevo dato
            
    # Si el usuario solo está entrando a la página a mirar (GET)
    else:
        form = CandidaturaForm() # Le entregamos un molde vacío
    
    # Enviamos tanto los festivales como el formulario al HTML
    contexto = {
        'eventos': festivales,
        'form': form
    }
    
    return render(request, 'eventos/lista_eventos.html', contexto)