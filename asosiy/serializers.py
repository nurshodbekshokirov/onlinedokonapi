from django.db.models import Avg
from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"

    def validated_chegirma(self,qiymat):
        if 0<qiymat<50:
            return qiymat
        raise serializers.ValidationError("Chegirma 0 dan kichik yoki 50 dan baland foizda bo'lishi mumkin emas")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Calculate average rating
        average_rating = Izoh.objects.filter(mahsulot=instance).aggregate(ortachasi=Avg('reyting'))[
            'ortachasi']
        # Add average rating to data dictionary
        data['ortacha_reyting'] = average_rating
        return data





class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = "__all__"
    def validated_reyting(self,qiymat):
        if 1<=qiymat<=5:
            return qiymat
        raise serializers.ValidationError("qiymat 1-5 oralig'ida bulishi kerak")




class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields  = "__all__"