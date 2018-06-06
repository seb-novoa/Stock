from django.test import TestCase
from django.urls import resolve
from persona.models import Areas, Puestos, Personas

from persona.views import persona_page
from persona.forms import PersonaGetForm

class AreaTestCase(TestCase):
    def setUp(self):
        Areas.objects.create(Area = "Desarollo")
        Areas.objects.create(Area = "Tica")

    def test_area_is_desarollo(self):
        des = Areas.objects.get(Area = "Desarollo")

        self.assertEqual(des.Area, "Desarollo")

    def test_area_is_Tica(self):
        tica = Areas.objects.get(Area = "Tica")
        self.assertEqual(tica.Area, "Tica")

    def test_area_have_not_the_same_id(self):
        des = Areas.objects.get(Area = "Desarollo")
        tica = Areas.objects.get(Area = "Tica")
        self.assertNotEqual(des.id, tica.id)

class PuestoTestCase(TestCase):
    def setUp(self):
        Puestos.objects.create(Puesto = "Alumno")

    def test_puesto_is_alumno(self):
        al = Puestos.objects.get(Puesto = "Alumno")
        self.assertEqual(al.Puesto, "Alumno")

class PersonasTestCase(TestCase):
    def setUp(self):
        Areas.objects.create(Area = "Desarollo")
        Puestos.objects.create(Puesto = "Alumno")

    def test_persona_is_created(self):
        area  = Areas.objects.get(Area = "Desarollo")
        puesto = Puestos.objects.get(Puesto = "Alumno")
        p1 = Personas.objects.create(Name = "Juan Perez", Area = area, Puesto = puesto)

        self.assertIsInstance(p1, Personas)
        self.assertIsInstance(p1.Area, Areas)
        self.assertIsInstance(p1.Puesto, Puestos)

    def test_gestor_is_instance_of_other_person(self):
        area  = Areas.objects.get(Area = "Desarollo")
        puesto = Puestos.objects.get(Puesto = "Alumno")

        p1 = Personas.objects.create(Name = "Juan Perez", Area = area, Puesto = puesto)
        p1.save()

        p2 = Personas.objects.create(Name = "Mario Bros" , Area = area, Puesto = puesto)
        p2.Gestor.add(p1)
        p2.save()

        self.assertEqual(p2.Gestor.last(), p1)

class PersonaPageTest(TestCase):
    def test_pesona_url_resolve_to_persona_page_view(self):
        found = resolve('/persona/')
        self.assertEqual(found.func, persona_page)


# class Setup_Persona(TestCase):
#     def setUp(self):
#         area = Areas.objects.get(Area = 'Desarollo')
#         puesto = Puesto.objects.get(Puesto = 'Alumno')
#         self.Persona = Persona.objects.create(Name = 'Juan Perez', Area = area, Puesto = puesto)
#
# class Persona_Form_test(TestCase):
#     def test_PersonaGetForm_valid(self):
#         form = PersonaGetForm(data = {
#             'Name'  : 'Juan Perez',
#             'Area'  : '',
#             'Puesto': '',
#         })
#
#         self.assertTrue(form.is_valid())
