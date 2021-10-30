from django.urls import path
from .views import recepcion, ReporteVentas, ReporteCompras


urlpatterns = [
    path('recepcion/', recepcion, name='recepcion'),
    path('reporte_ventas/', ReporteVentas.as_view(), name='reporte_ventas'),
    path('reporte_compras/', ReporteCompras.as_view(), name='reporte_compras'),
]