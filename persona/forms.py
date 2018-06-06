from django import forms
from persona.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ('Name', 'Area', 'Puesto')

class AreaForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ('Area', )


class PuestosForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = ('Puesto', )
