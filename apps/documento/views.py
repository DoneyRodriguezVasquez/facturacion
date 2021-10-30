from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from .xml_handler import Facturas
from .models import Factura, Resumen, Detalle
from django import forms
from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.utils import timezone
from datetime import timedelta

from xml.etree  import ElementTree as ET


def recepcion(request):
    
    if request.method == 'POST' and request.FILES:
        factura = Facturas(request.FILES['myFiles'], request.user)
        
        if factura.validar():
            factura.handle_uploaded_file()
            if len(factura.errors) > 0:
                for value in factura.errors:
                    messages.error(request, value)
                factura.errors.clear()
            else:
                form = Factura.objects.all().filter(fecha_carga__lte = timezone.now() + timedelta(days=1)).order_by('fecha_carga')[:10] 
                
                data = {'form': form}
                messages.success(request,'Documento agregado satisfactoriamente.')
                return HttpResponseRedirect('/documento/recepcion', request, data)

        else:
            messages.error(request, 'Error, Tipo de documento no válido')
            return render(request, 'documento/recepcion.html') 
    else:
        form = Factura.objects.all().filter(fecha_carga__lte = timezone.now() + timedelta(days=1)).order_by('fecha_carga')[:10] 
        data = {'form': form}
        return render(request, 'documento/recepcion.html', data)
    return render(request, 'documento/recepcion.html')


class ReporteVentas(LoginRequiredMixin, View):
    def get(self, request):
        start_date = '2021-09-01'
        end_date = '2021-09-30'
        data = Factura.objects.all().filter(FechaEmision__range = (start_date, end_date)).order_by('FechaEmision')

        ctx = {'data': data}
        return render(request, 'documento/reporte_ventas.html', ctx)


class ReporteCompras(LoginRequiredMixin, View):
    def get(self, request):
        start_date = '2021-09-01'
        end_date = '2021-09-30'
        data = Factura.objects.all().filter(FechaEmision__range = (start_date, end_date)).order_by('FechaEmision')

        ctx = {'data': data}
        return render(request, 'documento/reporte_compras.html', ctx)
    

