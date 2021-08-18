from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from apps.usuario.forms import UserForm
from django.contrib.auth import login, logout 
from django.views.generic import CreateView
from apps.usuario.models import Usuario


class Register(CreateView):
    model = Usuario
    form_class = UserForm
    template_name = 'usuario/register.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = Usuario(
                email = form.cleaned_data.get('email'),
                nombre = form.cleaned_data.get('nombre'),
                apellidos = form.cleaned_data.get('apellidos'),
                actividad = form.cleaned_data.get('actividad'),
                tipo_identificacion = form.cleaned_data.get('tipo_identificacion'),
                num_identificacion = form.cleaned_data.get('num_identificacion')
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('usuario:login')
        else:
            return render(request, self.template_name, {'form': form})

def login(request):
    return render(request, 'usuario:login.html')