from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import Register, login


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', Register.as_view(), name='register' ),
]