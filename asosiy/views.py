from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.permissions import *



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
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        izoh = Izoh.objects.filter(mahsulot__id=pk)
        serializer = IzohSerializer(izoh, many=True)
        return  Response(serializer.data)
    def post(self,request,pk):

        serializer = IzohSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user),
                            mahsulot=Mahsulot.objects.get(id=pk))
            natija = serializer.data
            natija['mahsulot'] = pk
            natija['profil'] = Profil.objects.get(user=request.user).id
            return Response(natija)
        return Response(serializer.errors)


class MahsulotApiVIew(APIView):
    def get(self, request, pk):
        mahsulo = Mahsulot.objects.filter(id=pk)
        serializer = MahsulotSerializer(mahsulo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
class MahsulotAPIVIEW(APIView):

    def get(self, request):
        soz = request.query_params.get('qidirish')
        if soz is None or soz == "":
            mahsulotlar = Mahsulot.objects.all()
        else:
            mahsulotlar = Mahsulot.objects.filter(nom__contains=soz)
        serializer = MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# Create your views here.
