from django.shortcuts import render, redirect
from persona.forms import PersonaForm
from persona.models import Personas

def persona_page(request):
    return render(request, 'persona.html', {})

def new_persona(request):
    return render(request, 'persona_new.html', {'form': PersonaForm()})

def save_persona(request):
    form = PersonaForm(data = request.POST )

    if form.is_valid():
        form.save()
        persona = Personas.objects.get(Name = form.data['Name'])
        persona.name_split()
        persona.save()
        return redirect(persona)
    else:
        return render(request, 'persona.html', {})

def view_persona(request, persona_id):
    persona = Personas.objects.get(id = persona_id)
    return render(request, 'view_persona.html', {'persona' : persona})
