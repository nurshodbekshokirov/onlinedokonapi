from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework.response import Response


class UserCreateApi(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            validated_data = serializer.data
            validated_data['id']=user.id
            return Response(validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfilCreateApi(APIView):
    def post(self,request):
        serializer = ProfilSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiview(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username = serializer.validated_data['username'],
                password = serializer.validated_data['password']
            )
            if user:
                login(request, user)
                return Response({"xabar":"Tizimga kiritildi"},status=status.HTTP_200_OK)
            return Response({"xabar":"Tizimga kiritilmadi"},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LogoutApiview(APIView):
    def get(self,request):
        logout(request)
        return Response({"xabar":"Tizimdan chiqarildi"})












# Create your views here.
