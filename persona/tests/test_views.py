from django.test import TestCase
from persona.models import Areas, Puestos, Personas
from . import base

class PersonaPageTest(TestCase):
    def test_new_persona_renders_persona_new_template(self):
        response = self.client.get('/persona/new/')
        self.assertTemplateUsed(response, 'persona_new.html')

class NewPersona(TestCase):
    def test_saving_a_POST_request(self):
        ar, pu = base.initial_Areas_and_Puestos()
        self.client.post('/persona/save/', data = {
            'Name'  : 'Nombre Apellido ApellidoMaterno',
            'Area'  : ar.id,
            'Puesto': pu.id,
        })

        self.assertEqual(Personas.objects.count(), 1)

        new_persona = Personas.objects.first()
        self.assertEqual(new_persona.Name, 'Nombre')
