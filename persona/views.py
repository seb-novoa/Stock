from django.shortcuts import render
from persona.forms import PersonaForm, AreaForm

def persona_page(request):
    return render(request, 'persona.html', {'form' : AreaForm()})

def new_persona(request):
    return render(request, 'persona_new.html', {'form': PersonaForm()})

def algo(request):
    pass
