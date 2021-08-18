from django import forms
from .models import *


class FacturaForm(forms.ModelForm):
    
    class Meta:
        model = Factura
        fields = ['clave', 'codigo_actividad', 'numero_consecutivo', 'fecha_emision', 'condicion_venta', 'medio_pago', 'plazo_credito', 'emisor_id', 'receptor_id', 'detalle_id', 'resumen_id']
        
