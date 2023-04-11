from django.db import models
from django.contrib.auth.models import User


class Profil(models.Model):
    ism = models.CharField(max_length=60)
    tel = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jins = models.CharField(max_length=10,choices=[("Erkak", "Erkak"), ("Ayol", "Ayol")])
    tugilgan_sana = models.DateField()


    def __str__(self):
        return self.ism

class Manzil(models.Model):
    shahar = models.CharField(max_length=100)
    manzil = models.CharField(max_length=100)
    asosiy = models.BooleanField()
    zipcode = models.CharField(max_length=50)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

    def __str__(self):
        return self.shahar

# Create your models here.
