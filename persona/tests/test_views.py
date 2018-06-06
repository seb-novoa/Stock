from django.test import TestCase
from persona.models import Areas, Puestos, Personas
from . import base
# import pdb; pdb.set_trace()

class PersonaPageTest(TestCase):
    def test_new_persona_renders_persona_new_template(self):
        response = self.client.get('/persona/new/')
        self.assertTemplateUsed(response, 'persona_new.html')

class NewPersona(TestCase):
    def valid_person_item(self, Nombre):
        ar, pu = base.initial_Areas_and_Puestos()
        response = self.client.post('/persona/save/', data = {
            'Name'  : Nombre,
            'Area'  : ar.id,
            'Puesto': pu.id
        })
        return response

    def invalid_person_item(self):
        ar, pu = base.initial_Areas_and_Puestos()
        response = self.client.post('/persona/save/', data = {
            'Name'  : '',
            'Area'  : ar.id,
            'Puesto': pu.id
        })
        return response

    def test_saving_a_POST_request(self):
        response = self.valid_person_item('Nombre Apellido ApellidoMaterno')
        self.assertEqual(Personas.objects.count(), 1)

        new_persona = Personas.objects.first()
        self.assertEqual(new_persona.Name, 'Nombre')

    def test_redirect_after_POST(self):
        response = self.valid_person_item('Nombre Apellido ApellidoMaterno')
        persona = Personas.objects.all()[0]
        self.assertRedirects(response, '/persona/%d/' %(persona.id))

    def test_invalid_person_items_arent_saved(self):
        response = self.invalid_person_item()
        self.assertEqual(Personas.objects.count(), 0)

    def test_for_invalid_input_renders_person_new_template(self):
        response = self.invalid_person_item()

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'persona_new.html')
