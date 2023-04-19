from django.urls import path
from .views import *
urlpatterns = [
    path("tanlangan/",TanlanganAPIVIEW.as_view()),
    path("tanlangan/<int:pk>/",TanlanganDetailApiView.as_view()),
    path("savat/",SavatAPIVIEW.as_view()),
    path("savat/<int:pk>/",SavatItemDetailAPiView.as_view()),
    path("<int:pk>/",BuyurtmaDetailView.as_view()),
    path("",BuyurtmalarApiview.as_view())

]