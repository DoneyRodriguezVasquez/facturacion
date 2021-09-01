from django.shortcuts import render
from .xml_handler import Facturas
from django import forms
from django.contrib import messages
from xml.etree  import ElementTree as ET


def recepcion(request):
    
    if request.method == 'POST' and request.FILES:
        factura = Facturas(request.FILES['myFiles'], request.user)
        
        if factura.validar():
            factura.handle_uploaded_file()
            if len(factura.errors) > 0:
                for value in factura.errors:
                    messages.error(request, value)
                    print(value)
                factura.errors.clear()
            
        else:
            messages.error(request, 'Error, Tipo de documento no válido')
            return render(request, 'documento/recepcion.html') 
    return render(request, 'documento/recepcion.html')


    

