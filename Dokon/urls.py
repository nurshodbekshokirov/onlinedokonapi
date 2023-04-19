
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Online Do'kon API",
      default_version='v1',
      description="O'quv maqsadlarida foydalanish uchun online do'kon API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact("Nurshodbek Shokirov,<nurshodbekshokirov@gmail.com>"),

   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('asosiy/', include('asosiy.urls')),
    path('buyurtma/', include('buyurtma.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('user/', include('userapp.urls')),
 ]
