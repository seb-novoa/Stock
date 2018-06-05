from django.db import models

class Areas(models.Model):
    Area = models.CharField(max_length = 30)

class Puestos(models.Model):
    Puesto = models.CharField(max_length = 30)

class Personas(models.Model):
    Name  = models.CharField(max_length = 50)
    Gestor  = models.ManyToManyField('self')
    Area    = models.ForeignKey(Areas, on_delete = models.CASCADE)
    Puesto  = models.ForeignKey(Puestos, on_delete = models. CASCADE)

    @property
    def gestorList(self):
        return list(self.gestor.all())
