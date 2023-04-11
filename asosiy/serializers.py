from rest_framework import serializers
from .models import *

class MahsulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahsulot
        fields = "__all__"


class IzohSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = "__all__"

class BolimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bolim
        fields  = "__all__"