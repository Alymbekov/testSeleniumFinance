from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test Selenium Finance",
      default_version='v1',
      description="API for parse data from finance.yahoo.com",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="alymbekovdastan1@gmail.com"),
      license=openapi.License(name="Open Source License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('api/v1/', include('finance.urls')),
]
