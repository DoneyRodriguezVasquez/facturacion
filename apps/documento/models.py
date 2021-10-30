from django.db import models
from django.conf import settings


class Emisor(models.Model):
    Nombre = models.CharField('Nombre', max_length=200, null=True)
    NombreComercial = models.CharField('Nombre Comercial',max_length=500, null=True)
    CorreoElectronico = models.CharField('Email',max_length=200, blank=False, null=False)   
    Numero = models.BigIntegerField('Numero de Identificación',primary_key=True, unique=True, blank=False, null=False)
    Tipo = models.IntegerField('Tipo de Identificación',blank=False, null=False)
    Provincia = models.CharField('Provincia',max_length=200, null=True)
    Canton = models.CharField('Cantón',max_length=200, null=True)
    Distrito = models.CharField('Distrito',max_length=200, null=True)
    Barrio = models.CharField('Barrio',max_length=200, null=True)
    OtrasSenas = models.CharField('Otras señas',max_length=400, null=True)
    CodigoPais = models.IntegerField('Código País', null=True)
    NumTelefono = models.CharField('Teléfono',max_length=20, null=False, blank=False)

    class Meta:
        verbose_name = 'Emisor'
        verbose_name_plural = 'Emisores'   
        ordering = ['Nombre']
        

    def __str__(self):
        return f'{str(self.Nombre)}'                                 
  
    def get_id(self):
        return self.Numero

class Detalle(models.Model):
    id = models.AutoField(primary_key=True)
    iva13_bienes = models.FloatField('iva13_bienes', null=True)
    iva13_servicios = models.FloatField('iva13_servicios', null=True)
    iva4_bienes = models.FloatField('iva4_bienes', null=True)
    iva4_servicios = models.FloatField('iva4_servicios', null=True)
    iva2_bienes = models.FloatField('iva2_bienes', null=True)
    iva2_servicios = models.FloatField('iva2_servicios', null=True)
    iva1_bienes = models.FloatField('iva1_bienes', null=True)
    iva1_servicios = models.FloatField('iva1_servicios', null=True)
    subtotal_bienes = models.FloatField('subtotal_bienes', null=True)
    subtotal_serv = models.FloatField('subtotal_servicios', null=True)
    total_bienes = models.FloatField('total_bienes', null=True)
    total_serv = models.FloatField('total_servicios', null=True)
    SubTotal = models.FloatField('Subtotal', blank=False, null=False)
    ImpuestoNeto = models.FloatField('Impuesto Neto', blank=False, null=False)
    MontoTotal = models.FloatField('Monto total linea', blank=False, null=False)

    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        return str(self.id) or ''
 
    
    def get_id(self):
        return self.id

class Resumen(models.Model):
    id = models.AutoField(primary_key=True)
    CodigoMoneda =  models.CharField('Código moneda', max_length=64, null=False)
    TipoCambio = models.FloatField('Tipo de cambio', null=False)
    TotalServGravados = models.FloatField('Total servicios gravados', null=True)
    TotalServExentos = models.FloatField('Total servicios exentos', null=True)
    TotalServExonerado = models.FloatField('Total servicios exonerados', null=True)
    TotalMercanciasGravadas = models.FloatField('Total mercancias gravadas', null=True)
    TotalMercanciasExentas = models.FloatField('Total mercancias exentas', null=True)
    TotalMercExonerada = models.FloatField('Total mercancias exoneradas', null=True)
    TotalGravado = models.FloatField('Total gravado', null=True)
    TotalExento = models.FloatField('Total exento', null=True)
    TotalExonerado = models.FloatField('Total exonerado', null=True)
    TotalVenta = models.FloatField('Total venta', blank=False, null=False)
    TotalDescuentos = models.FloatField('Total descuento', null=True)
    TotalVentaNeta = models.FloatField('Total venta neta', blank=False, null=False)
    TotalImpuesto = models.FloatField('Total impuesto', blank=False, null=False)
    TotalIVADevuelto = models.FloatField('Total IVA Devuelto', blank=True, null=True)
    TotalOtrosCargos = models.FloatField('Total otros cargos', null=True)
    TotalComprobante = models.FloatField('Total comprobante', blank=False, null=False)

    class Meta:
        verbose_name = 'Resumen'
        verbose_name_plural = 'Resumenes'

    def __str__(self):
        return str(self.id) or ''
    
    def get_id(self):
        return self.id

class Factura(models.Model):
    #id = models.AutoField(primary_key = True)
    Clave = models.CharField('Clave',max_length = 200, primary_key = True, unique = True, blank = False, null = False)
    CodigoActividad = models.IntegerField('Código de actividad', null=True)
    NumeroConsecutivo = models.BigIntegerField('Número de consecutivo', null=True)
    FechaEmision = models.DateTimeField ('Fecha de emisión', blank = False, null = False)
    fecha_carga = models.DateTimeField('Fecha de carga', blank = False, null = False)
    CondicionVenta = models.IntegerField('Condición de venta', null=True)
    MedioPago = models.IntegerField('Medio de pago', null=True)
    emisor = models.ForeignKey(Emisor, on_delete = models.CASCADE)
    detalle = models.ForeignKey(Detalle, on_delete=models.CASCADE)
    resumen = models.ForeignKey(Resumen, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'
    
    def __str__(self):
        return str(self.NumeroConsecutivo) if self.NumeroConsecutivo else ''
        