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

# Create your views here.
