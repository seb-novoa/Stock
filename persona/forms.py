from django import forms
from persona.models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Personas
        fields = ('Name', 'Area', 'Puesto')

    def save(self, commit = True):
        instance = super(PersonaForm, self).save(commit = False)
        instance.name_split()
        if commit:
            instance.save()
        return instance

class AreaForm(forms.ModelForm):
    CDC = forms.IntegerField(required = False)
    class Meta:
        model = Areas
        fields = ('CDC', 'Area', )
        error_massages = {
            'my_unique_field' : {
                'unique' : 'Esta campo ya esta registrado'
            },
        }

    def form_valid(self, form):
        area = slugify(form.cleaned_data['Area'])
        try:
            area = Areas.objects.get(Area = area)
        except Area.DoesNotExist:
            raise ValidationError('Esta Área ya está registrada')


class PuestosForm(forms.ModelForm):
    class Meta:
        model = Puestos
        fields = ('Puesto', )
