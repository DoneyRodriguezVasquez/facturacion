from django.urls import path
from .views import recepcion


urlpatterns = [
    path('recepcion/', recepcion, name='recepcion'),
]