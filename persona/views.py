from django.shortcuts import render, redirect, get_object_or_404
from persona.forms import PersonaForm, AreaForm, PuestoForm
from persona.models import Personas, Areas

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

# Editar areas y puestos

def editar_area_puesto(request):
    return render(request, 'edit_area_puesto.html', {'AreaForm' : AreaForm})

def editar_area(request):
    form = AreaForm(data = request.POST)
    area = Areas.objects.get(Area = form.data['Area'])
    formInstance = AreaForm(instance = area)
    return render(request, 'edit_area.html', {'area_id':area.id , 'formInstance' : formInstance})

def save_edit_area(request, area_id = None):
    instance = get_object_or_404(Areas, id = area_id)
    form = AreaForm(request.POST or None, instance = instance )
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return redirect('editar_area_puesto')

    else:
         return render(request, 'edit_area.html', {'formInstance' : form})


def edit_puesto(request):
    pass
