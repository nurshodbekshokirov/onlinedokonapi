from django.db import models
from userapp.models import Profil


class Bolim(models.Model):
    nom = models.CharField(max_length=70)
    rasm = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    narx = models.PositiveIntegerField()
    brend = models.CharField(max_length=50)
    chegirma = models.PositiveSmallIntegerField()
    davlat = models.CharField(max_length=50)
    rasm = models.FileField(null=True, blank=True)
    batafsil = models.CharField(max_length=100)
    mavjud = models.BooleanField()

    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Izoh(models.Model):
    matn = models.TextField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    reyting = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.matn



# Create your models here.
