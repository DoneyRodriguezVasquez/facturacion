from django.db import models
from django.db.models.fields import AutoField


class Emisor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200, blank=False, null=False)
    identificacion = models.CharField('Identificación',max_length=200, blank=False, null=False)
    num_identificacion = models.IntegerField('Numero de Identificación', blank=False, null=False)
    tipo_identificacion = models.IntegerField('Tipo de Identificación',blank=False, null=False)
    nombre_comercial = models.CharField('Nombre Comercial',max_length=500)
    ubicacion = models.CharField('Ubicación',max_length=500, null=False, blank=False)
    provincia = models.CharField('Provincia',max_length=200, blank=False, null=False)
    canton = models.CharField('Cantón',max_length=200, blank=False, null=False)
    distrito = models.CharField('Distrito',max_length=200, blank=False, null=False)
    otras_senas = models.CharField('Otras señas',max_length=400, blank=False, null=False)
    telefono = models.CharField('Teléfono',max_length=20, null=False, blank=False)
    correo_electronico = models.CharField('Email',max_length=200, blank=False, null=False)   

    class Meta:
        verbose_name = 'Emisor'
        verbose_name_plural = 'Emisores'   
        ordering = ['nombre']

    def __str__(self):
        return self.nombre                                       

class Receptor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length=200, blank=False, null=False)
    identificacion = models.CharField('Identificación',max_length=200, blank=False, null=False)
    num_identificacion = models.IntegerField('Numero de Identificación', blank=False, null=False)
    tipo_identificacion = models.IntegerField('Tipo de Identificación',blank=False, null=False)
    nombre_comercial = models.CharField('Nombre Comercial',max_length=500)
    ubicacion = models.CharField('Ubicación',max_length=500, null=False, blank=False)
    provincia = models.CharField('Provincia',max_length=200, blank=False, null=False)
    canton = models.CharField('Cantón',max_length=200, blank=False, null=False)
    distrito = models.CharField('Distrito',max_length=200, blank=False, null=False)
    otras_senas = models.CharField('Otras señas',max_length=400, blank=False, null=False)
    telefono = models.CharField('Teléfono',max_length=20, null=False, blank=False)
    correo_electronico = models.CharField('Email',max_length=200, blank=False, null=False)   

    class Meta:
        verbose_name = 'Receptor'
        verbose_name_plural = 'Receptores'
        ordering = ['nombre']

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    numero_linea = models.IntegerField(blank=False, null=False)
    cantidad = models.IntegerField(blank=False, null=False)
    detalle = models.CharField(max_length=200, blank=False, null=False)
    precio_unitario = models.FloatField(blank=False, null=False)
    monto_total = models.FloatField(blank=False, null=False)
    subtotal = models.FloatField(blank=False, null=False)
    codigo_impuesto = models.IntegerField(blank=False, null=False)
    codigo_tarifa = models.IntegerField(blank=False, null=False)
    tarifa = models.IntegerField(blank=False, null=False)
    monto = models.FloatField(blank=False, null=False)
    impuesto_neto = models.FloatField(blank=False, null=False)
    monto_total_linea = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

class Resumen(models.Model):
    id = models.AutoField(primary_key=True)
    total_serv_gravados = models.FloatField(blank=False, null=False)
    total_serv_exentos = models.FloatField(blank=False, null=False)
    total_serv_exonerados = models.FloatField(blank=False, null=False)
    total_mercancias_gravadas = models.FloatField(blank=False, null=False)
    total_mercancias_exentas = models.FloatField(blank=False, null=False)
    total_mercancias_exoneradas = models.FloatField(blank=False, null=False)
    total_gravado = models.FloatField(blank=False, null=False)
    total_exento = models.FloatField(blank=False, null=False)
    total_exonerado = models.FloatField(blank=False, null=False)
    total_venta = models.FloatField(blank=False, null=False)
    total_descuentos = models.FloatField(blank=False, null=False)
    total_venta_neta = models.FloatField(blank=False, null=False)
    total_impuestos = models.FloatField(blank=False, null=False)
    total_comprobante = models.FloatField(blank=False, null=False)

    class Meta:
        verbose_name = 'Resumen'
        verbose_name_plural = 'Resumenes'

class Factura(models.Model):
    id = models.AutoField(primary_key = True)
    clave = models.CharField('Clave',max_length = 200, blank = False, null = False)
    codigo_actividad = models.IntegerField('Código de actividad')
    numero_consecutivo = models.IntegerField('Número de consecutivo')
    fecha_emision = models.DateField('Fecha de emisión', blank = False, null = False)
    condicion_venta = models.IntegerField('Condición de venta')
    medio_pago = models.IntegerField('Medio de pago')
    plazo_credito = models.IntegerField('Plazo de crédito')
    emisor_id = models.ForeignKey(Emisor, on_delete = models.CASCADE)
    receptor_id = models.ForeignKey(Receptor, on_delete=models.CASCADE)
    detalle_id = models.ForeignKey(Detalle, on_delete=models.CASCADE)
    resumen_id = models.ForeignKey(Resumen, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
    