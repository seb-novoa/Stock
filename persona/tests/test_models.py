from django.test import TestCase

from persona.models import Areas, Puestos, Personas
from . import base 

class PersonaTestCase (TestCase):
    def test_name_split_to_get_lastname(self):
        ar, pu = base.initial_Areas_and_Puestos()
        p1 = Personas.objects.create(Name = 'Nombre Apellido ApellidoMaterno', Area = ar, Puesto = pu)

        self.assertEqual(p1.Name, 'Nombre Apellido ApellidoMaterno')

        p1.name_split()
        self.assertEqual(p1.Name, 'Nombre')
        self.assertEqual(p1.Lastname, 'Apellido')
        self.assertEqual(p1.MotherLastname, 'ApellidoMaterno')
