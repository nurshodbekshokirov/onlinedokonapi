from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status



class BolimlarApiview(APIView):
    def get(self, request):
        bolimlar = Bolim.objects.all()
        serializer = BolimSerializer(bolimlar, many=True)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = BolimSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BolimApiview(APIView):
    def get(self,request,pk):
        mahsulotlar = Mahsulot.objects.filter(bolim__id=pk)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)
class ChegirmaliAPIview(APIView):
    def get(self,request):
        chegirma = Mahsulot.objects.filter(chegirma__gt=0).order_by('chegirma')[:12]
        serializer = MahsulotSerializer(chegirma, many=True)
        return Response(serializer.data)

class IzohAPIview(APIView):
    def get(self, request, pk):
        izoh = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izoh, many=True)
        return  Response(serializer.data)
class MahsulotApiVIew(APIView):
    def get(self, request, pk):
        mahsulo = Mahsulot.objects.filter(id=pk)
        serializer = MahsulotSerializer(mahsulo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Create your views here.
