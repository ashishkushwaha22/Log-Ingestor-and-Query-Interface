"""
URL configuration for logInjestorProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from logInjestor.views import LogEntryViewSet, LoginAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Create a router and register the LogEntryViewSet
router = DefaultRouter()
router.register(r'', LogEntryViewSet, basename='logs')

"""
    Django project URL patterns.

    Attributes:
        admin (path): URL pattern for the Django admin site.
        router.urls (path): URL patterns for LogEntry API views.

    Example:
        To access the Django admin site:
        https://yourdomain.com/admin/

        To access LogEntry API views:
        https://yourdomain.com/
"""

schema_view = get_schema_view(
   openapi.Info(
      title="Log Ingestor API",
      default_version='v1',
      description="API documentation for Log Ingestor",
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('', include(router.urls)),

]
