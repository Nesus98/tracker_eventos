from django.shortcuts import render, redirect, get_object_or_404
from .models import Evento, Candidatura
from .forms import CandidaturaForm, EventoForm # <-- Importamos ambos formularios

# 1. La vista principal ahora está limpia, solo lee la base de datos.
def lista_eventos(request):
    festivales = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': festivales})

# 2. Nueva vista: Crear Evento
def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventoForm()
    
    return render(request, 'eventos/crear_evento.html', {'form': form})

# 3. Nueva vista: Crear Candidatura
def crear_candidatura(request):
    if request.method == 'POST':
        form = CandidaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = CandidaturaForm()
        
    return render(request, 'eventos/crear_candidatura.html', {'form': form})

# (Mantén tu función eliminar_candidatura y las demás que ya tenías abajo)


def eliminar_candidatura(request, pk):
    candidatura = get_object_or_404(Candidatura, pk=pk)

    if request.method == 'POST':
        candidatura.delete()
        return redirect('lista_eventos')

    return render(request, 'eventos/confirmar_eliminacion.html', {
        'objeto': candidatura,
        'titulo': 'Eliminar candidatura',
        'mensaje': f'¿Eliminar la candidatura "{candidatura.puesto}" en {candidatura.evento.nombre}?',
    })

# Añade esta función al final de eventos/views.py
def editar_evento(request, pk):
    # 1. Buscamos el festival específico usando el 'pk' (ID) que viene de la URL
    evento = get_object_or_404(Evento, id=pk)
    
    # 2. Si el usuario procesa el formulario editado (POST)
    if request.method == 'POST':
        # Pasamos los datos nuevos pero vinculados a la 'instance' (el evento viejo)
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
            
    # 3. Si solo entra a la página a editar (GET)
    else:
        # Cargamos el molde PRE-RELLENADO con los datos actuales del festival
        form = EventoForm(instance=evento)
        
    # Reutilizamos la misma plantilla HTML de crear_evento, ya que tiene los mismos campos
    return render(request, 'eventos/crear_evento.html', {'form': form})
    # Añade esta función al final de eventos/views.py
def eliminar_evento(request, pk):
    # Buscamos el festival exacto usando su ID (pk)
    evento = get_object_or_404(Evento, id=pk)
    
    # Lo eliminamos de la base de datos
    evento.delete()
    
    # Volvemos a la pantalla principal
    return redirect('lista_eventos')

# Añade esta función al final de eventos/views.py
def editar_candidatura(request, pk):
    # 1. Buscamos la candidatura específica por su ID (pk)
    candidatura = get_object_or_404(Candidatura, id=pk)
    
    # 2. Si el usuario envía el formulario con los cambios (POST)
    if request.method == 'POST':
        # Pasamos los datos del POST pero vinculados a la candidatura existente
        form = CandidaturaForm(request.POST, instance=candidatura)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
            
    # 3. Si solo entra a la página de edición (GET)
    else:
        # Cargamos el molde con los datos actuales de la candidatura (puesto, estado, notas...)
        form = CandidaturaForm(instance=candidatura)
        
    # Reutilizamos la misma plantilla responsiva de crear_candidatura.html
    return render(request, 'eventos/crear_candidatura.html', {'form': form})