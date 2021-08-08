from django.contrib import admin
from .models import *


admin.site.register(Factura)
admin.site.register(Emisor)
admin.site.register(Receptor)
admin.site.register(Detalle)
admin.site.register(Resumen)
