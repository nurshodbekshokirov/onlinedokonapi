from django.urls import path
from .views import *
urlpatterns = [
    path('bolimlar/', BolimlarApiview.as_view()),
    path('bolim/<int:pk>/', BolimApiview.as_view()),
    path("chegirmalilar/", ChegirmaliAPIview.as_view()),
    path("mahsulot/<int:pk>/izohlar/", IzohAPIview.as_view()),
    path("mahsulot/<int:pk>/", MahsulotApiVIew.as_view()),
    path("mahsulotlar/", MahsulotAPIVIEW.as_view()),
]