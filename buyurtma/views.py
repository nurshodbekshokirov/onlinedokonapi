from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class TanlanganAPIVIEW(APIView):
    def get(self,request):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user)
        serializer = TanlanganSerializer(tanlangan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SavatAPIVIEW(APIView):
    def get(self,request):
        savat = Savat.objects.get(profil__user=request.user)
        savat_itemlar = SavatItem.objects.filter(savat=savat)
        serializer = SavatItemSerializer(savat_itemlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = SavatItemSerializer(data=request.data)
        savat = Savat.objects.filter(profil__user=request.user)
        if not savat:
            Savat.objects.create(profil=Profil.objects.get(user=request))
        savat = Savat.objects.get(profil__user=request.user)
        if serializer.is_valid():
            serializer.save(savat=savat)
            return Response(serializer.data)
        return Response(serializer.errors)

class BuyurtmaDetailView(APIView):
    def get(self,request,pk):
        buyurtma = Buyurtma.objects.get(id=pk)
        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data)

# Create your views here.
