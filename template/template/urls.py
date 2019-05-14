"""template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import include, path, re_path
from django.conf.urls import url
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema


schema_view = get_schema_view(
   openapi.Info(
      title="Template API",
      default_version='v1',
      description="FuelPrediction service API description",
   ),
)

@swagger_auto_schema(method='get', auto_schema=None)
@api_view(['GET'])
def plain_view(request):
    pass

@swagger_auto_schema(method='get')
@api_view(['GET'])
def version_view(request):
    return Response(settings.API_VERSION, status=status.HTTP_200_OK)

urlpatterns = [
    url(r'streaming/', include('streaming.urls')),
    path('myapp/', include('myapp.urls')),
    path(r'plain/', plain_view),
    path('admin/', admin.site.urls),
    url(r'v2/swagger', schema_view.with_ui(), name="schema_view"),
    url(r'v2/api-docs', schema_view.with_ui(), name='schema-view'),
    url('service/getVersion', version_view),
]

