from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^prueba/', prueba, name="prueba"),
]
