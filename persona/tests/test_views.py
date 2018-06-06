from django.test import TestCase
from persona.models import Areas, Puestos, Personas

# registrar area y puesto
def initial_Areas_and_Puestos():
    ar = Areas.objects.create(Area = 'Area1')
    pu = Puestos.objects.create(Puesto = 'Puesto1')
    return ar, pu
    
class NewPersona(TestCase):
    def test_name_split_to_get_lastname(self):
        ar, pu = initial_Areas_and_Puestos()
        p1 = Personas.objects.create(Name = 'Nombre Apellido', Area = ar, Puesto = pu)

        self.assertEqual(p1.Name, 'Nombre Apellido')

        p1.name_split()
        self.assertEqual(p1.Name, 'Nombre')
        self.assertEqual(p1.Lastname, 'Apellido')
