from django.test import TestCase
from persona.models import Areas, Puestos, Personas
from . import base
# import pdb; pdb.set_trace()

class PersonaPageTest(TestCase):
    def test_new_persona_renders_persona_new_template(self):
        response = self.client.get('/persona/new/')
        self.assertTemplateUsed(response, 'persona_new.html')

    def test_new_area_renders_area_new_template(self):
        response = self.client.get('/persona/area/')
        self.assertTemplateUsed(response, 'area_page.html')

    def test_new_puesto_renders_puesto_new_template(self):
        response = self.client.get('/persona/puesto/')
        self.assertTemplateUsed(response, 'puesto_page.html')

    def test_edit_area_puesto(self):
        response = self.client.get('/persona/editar/')
        self.assertTemplateUsed(response, 'edit_area_puesto.html')


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

class NewArea(TestCase):
    def valid_area_item(self, CDC, Area):
        response = self.client.post('/persona/area/save/', data = {
            'CDC' : CDC,
            'Area': Area
        })
        return response

    def invalid_area_item(self):
        response = self.client.post('/persona/area/save/', data = {
            'CDC' : '',
            'Area': ''
        })
        return response

    def test_saving_a_POST_request(self):
        response = self.valid_area_item(1, 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

    def test_saving_a_Post_request_without_CDC(self):
        response = self.client.post('/persona/area/save/', data = {
            'CDC' : '',
            'Area': 'Area1'
        })
        self.assertEqual(Areas.objects.count(), 1)

    def test_dont_save_the_same(self):
        r1 = self.valid_area_item(1, 'Area1')
        r2 = self.valid_area_item(1, 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

        r2 = self.valid_area_item(1, 'Area2')
        self.assertEqual(Areas.objects.count(), 1)

        r2 = self.valid_area_item(2, 'Area1')
        self.assertEqual(Areas.objects.count(), 1)

    def test_redirect_after_POST(self):
        response = self.valid_area_item(1, 'Area1')
        self.assertRedirects(response, '/persona/')

    def test_invalid_area_items_arent_saved(self):
        response = self.invalid_area_item()
        self.assertEqual(Areas.objects.count(), 0)

    def test_duplicate_item_validation_errors_up_on_area_page(self):
        area1 = self.valid_area_item(1 , 'Area1')
        response = self.valid_area_item(1 , 'Area1')
        expected_error_Area = 'El campo Area ya esta registrado'
        expected_error_CDC = 'El campo CDC ya esta registrado'

        self.assertContains(response, expected_error_Area)
        self.assertContains(response, expected_error_CDC)
        self.assertTemplateUsed(response, 'area_page.html')
        self.assertEqual(Areas.objects.count(), 1)

    def test_edit_area_search_an_area_objects(self):
        self.valid_area_item(1, 'Area1')
        response = self.client.post('/persona/editar/area/', data = {
            'Area' : 'Area1'
        })

        self.assertTemplateUsed(response, 'edit_area.html')
        self.assertContains(response, 'Area1')

    def test_edit_area_save_changes(self):
        self.valid_area_item(1, 'Area1')
        response = self.client.post('/persona/editar/area/1/', data = {
            'CDC' : 2,
            'Area': 'Area1'
        })

        area = Areas.objects.first()
        self.assertEqual(area.CDC, 2)


class NewPuesto(TestCase):
    def valid_puesto_item(self, Puesto):
        response = self.client.post('/persona/puesto/save/', data = {
            'Puesto' : Puesto
        })
        return response

    def test_redirect_after_POST(self):
        response = self.valid_puesto_item('Puesto1')
        self.assertRedirects(response, '/persona/')

    def test_saving_a_POST_request(self):
        p1 = self.valid_puesto_item('Puesto1')
        self.assertEqual(Puestos.objects.count(), 1)

    def test_dont_save_the_same(self):
        p1 = self.valid_puesto_item('')
        self.assertEqual(Puestos.objects.count(), 0)

    def test_dont_save_the_same(self):
        p1 = self.valid_puesto_item('Puesto1')
        p2 = self.valid_puesto_item('Puesto1')

        self.assertEqual(Puestos.objects.count(), 1)

    def test_duplicate_item_validation_errors_up_on_puesto_page(self):
        p1 = self.valid_puesto_item('Puesto1')
        response = self.valid_puesto_item('Puesto1')
        expected_error = 'El Puesto ya ha sido registrado'

        self.assertContains(response, expected_error)
        self.assertTemplateUsed(response, 'puesto_page.html')
        self.assertEqual(Puestos.objects.count(), 1)
