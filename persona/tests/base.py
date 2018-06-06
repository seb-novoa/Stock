from persona.models import Areas, Puestos, Personas

def initial_Areas_and_Puestos():
    ar = Areas.objects.create(Area = 'Area1')
    pu = Puestos.objects.create(Puesto = 'Puesto1')
    return ar, pu
