from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^encode', views.Base64View.as_view(), name='encoder'),
    url(r'^cumulateddistance', views.VectorOperation.as_view(), name='cumulateddistance'),
]