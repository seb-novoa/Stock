from django.shortcuts import render, redirect
from persona.forms import PersonaForm, AreaForm, PuestoForm
from persona.models import Personas

def persona_page(request):
    return render(request, 'persona.html', {})

def new_persona(request):
    return render(request, 'persona_new.html', {'form': PersonaForm()})

def save_persona(request):
    form = PersonaForm(data = request.POST )
    if form.is_valid():
        persona = form.save()
        return redirect(persona)
    else:
        return render(request, 'persona_new.html', {'form': PersonaForm()})

def view_persona(request, persona_id):
    persona = Personas.objects.get(id = persona_id)
    return render(request, 'view_persona.html', {'persona' : persona})

# Areas
def area_page(request):
    return render (request, 'area_page.html', {'form' : AreaForm()})

def save_area(request):
    form = AreaForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('persona_page')
    else:
        return render (request, 'area_page.html', {'form' : form })

# Puestos
def puesto_page(request):
    return render(request, 'puesto_page.html', {'form' : PuestoForm()})

def save_puesto(request):
    form = PuestoForm(data = request.POST)
    if form.is_valid():
        form.save()
        return redirect('persona_page')
    else:
        return render(request, 'puesto_page.html', {'form' : form})
