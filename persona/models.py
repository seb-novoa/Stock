from django.db import models
from django.urls import reverse

class Areas(models.Model):
    CDC  = models.IntegerField(null = True)
    Area = models.CharField(max_length = 30)

    def __str__(self):
        return self.Area


class Puestos(models.Model):
    Puesto = models.CharField(max_length = 30)

    def __str__(self):
        return self.Puesto

class Personas(models.Model):
    Name  = models.CharField(max_length = 50)
    Lastname = models.CharField(max_length = 30, null = True)
    MotherLastname = models.CharField(max_length = 30, null = True)
    Gestor  = models.ManyToManyField('self', null = True)
    Area    = models.ForeignKey(Areas, on_delete = models.CASCADE)
    Puesto  = models.ForeignKey(Puestos, on_delete = models. CASCADE)

    @property
    def gestorList(self):
        return list(self.gestor.all())

    def name_split(self):
        names = str.split(self.Name)
        self.Name = names[0]
        self.Lastname = names[1]
        self.MotherLastname = ''.join(names[2:])

    def get_absolute_url(self):
        return reverse('view_persona', args=[self.id])
