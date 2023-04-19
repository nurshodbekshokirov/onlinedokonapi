from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from userapp.models import *

class TanlanganAPIVIEW(APIView):
    def get(self,request):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user)
        serializer = TanlanganSerializer(tanlangan, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TanlanganDetailApiView(APIView):
    def get(self,request,pk):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user, id=pk)

        serializer = TanlanganSerializer(tanlangan, many=True)

        return Response(serializer.data)
    def delete(self,request, pk):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user, id=pk)
        if tanlangan:
            tanlangan.delete()
            return Response({"xabar":"ochirildi"})
        return Response({"xabar":"bunday tanlangan mahsulot yo'q"})
    def put(self,request,pk):
        tanlangan = Tanlangan.objects.filter(profil__user=request.user, id=pk)
        if tanlangan:
            tanlangan = tanlangan[0]
            serializer = TanlanganSerializer(tanlangan,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response({'error': 'Ma\'lumot topilmadi'}, status=status.HTTP_404_NOT_FOUND)




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

class SavatItemDetailAPiView(APIView):
    def get(self,request, pk):
        savat = SavatItem.objects.filter(savat__profil__user=request.user, id=pk)
        serializer = SavatItemSerializer(savat, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self,request,pk):
        savat = SavatItem.objects.filter(savat__profil__user=request.user, id=pk)
        if not savat:
            return Response({"xabar":"savat topilmadi"})
        savat.delete()
        return Response({"xabar": "savat o'chirildi"})
    def put(self,request, pk):
        savat = SavatItem.objects.filter(savat__profil__user=request.user, id=pk)[0]
        if not savat:
            return Response({"xabar":"savat topilmadi"})


        serializer = SavatItemSerializer(savat, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class BuyurtmaDetailView(APIView):
    def get(self,request,pk):
        buyurtma = Buyurtma.objects.get(id=pk)
        serializer = BuyurtmaSerializer(buyurtma)
        return Response(serializer.data)
class BuyurtmalarApiview(APIView):
    def get(self,request):
        buyurtma = Buyurtma.objects.filter(profil__user=request.user)
        serializer  = BuyurtmaSerializer(buyurtma, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self,request):
        serializer = BuyurtmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors )


# Create your views here.
