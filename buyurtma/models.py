from django.utils import timezone

from django.db import models
from userapp.models import Profil
from asosiy.models import Mahsulot

class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Savat(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana= models.DateTimeField(default=timezone.now)



class SavatItem(models.Model):
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE, related_name='savat_items')
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveIntegerField(default=1)
    yetkazish_sana = models.DateField()
    umumiy_narx = models.DecimalField(decimal_places=2, max_digits=10)

    def save(self, *args, **kwargs):
        self.umumiy_narx = (self.mahsulot.narx - self.mahsulot.narx * self.mahsulot.chegirma / 100) * self.miqdor
        super().save(*args, **kwargs)


class Buyurtma(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    savat = models.ForeignKey(Savat, on_delete=models.CASCADE)
    berilgan_sana = models.DateTimeField(default=timezone.now)
    manzil = models.CharField(max_length=255)
    yetkazish_sana = models.DateField()






