from django.urls import path
from .views import *
urlpatterns = [
    path('create/', UserCreateApi.as_view()),
    path('profil/create/', ProfilCreateApi.as_view()),
    path('login/', LoginApiview.as_view()),
    path('logout/', LogoutApiview.as_view()),
    path('profil/<int:pk>/', ProfilDetailAPIVIEW.as_view()),
]