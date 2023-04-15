
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('user/', include('userapp.urls')),
 ]
