from rest_framework import serializers
from .models import *

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profil
        fields = "__all__"

class ManzilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manzil
        fields = "__all__"