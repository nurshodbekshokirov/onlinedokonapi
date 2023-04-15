from django.db import models
from userapp.models import Profil
from asosiy.models import Mahsulot

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)


class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    yetkazish_kuni = models.PositiveSmallIntegerField(default=4)
    yetkazish_puli = models.FloatField(default=0)



