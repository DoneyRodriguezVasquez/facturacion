from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from apps.usuario.forms import UserForm, LoginForm
from django.contrib.auth import login, logout, authenticate 
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
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
            logout(request)
            return redirect('login')
        else:
            return render(request, self.template_name, {'form': form})


def login(request):
    context={}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form=LoginForm()
        context = {'form': form}
    return render(request, 'usuario/login.html', context)


def logout(request):
    logout(request)
    return HttpResponseRedirect('login')