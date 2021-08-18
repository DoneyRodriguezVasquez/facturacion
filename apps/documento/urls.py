from django.urls import path
from .views import Documento


urlpatterns = [
    path('documento/', Documento, name='index'),
]