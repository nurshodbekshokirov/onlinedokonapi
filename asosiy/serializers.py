from django.db.models import Avg
from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"

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

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields  = "__all__"