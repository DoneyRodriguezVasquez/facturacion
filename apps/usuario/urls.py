from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Register


urlpatterns = [
    path('register/', Register.as_view(), name='register' ),
]