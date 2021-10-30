# Generated by Django 3.2.6 on 2021-09-02 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('iva13_bienes', models.FloatField(null=True, verbose_name='iva13_bienes')),
                ('iva13_servicios', models.FloatField(null=True, verbose_name='iva13_servicios')),
                ('iva4_bienes', models.FloatField(null=True, verbose_name='iva4_bienes')),
                ('iva4_servicios', models.FloatField(null=True, verbose_name='iva4_servicios')),
                ('iva2_bienes', models.FloatField(null=True, verbose_name='iva2_bienes')),
                ('iva2_servicios', models.FloatField(null=True, verbose_name='iva2_servicios')),
                ('iva1_bienes', models.FloatField(null=True, verbose_name='iva1_bienes')),
                ('iva1_servicios', models.FloatField(null=True, verbose_name='iva1_servicios')),
                ('subtotal_bienes', models.FloatField(null=True, verbose_name='subtotal_bienes')),
                ('subtotal_serv', models.FloatField(null=True, verbose_name='subtotal_servicios')),
                ('total_bienes', models.FloatField(null=True, verbose_name='total_bienes')),
                ('total_serv', models.FloatField(null=True, verbose_name='total_servicios')),
                ('SubTotal', models.FloatField(verbose_name='Subtotal')),
                ('ImpuestoNeto', models.FloatField(verbose_name='Impuesto Neto')),
                ('MontoTotal', models.FloatField(verbose_name='Monto total linea')),
            ],
            options={
                'verbose_name': 'Detalle',
                'verbose_name_plural': 'Detalles',
            },
        ),
        migrations.CreateModel(
            name='Emisor',
            fields=[
                ('Nombre', models.CharField(max_length=200, null=True, verbose_name='Nombre')),
                ('NombreComercial', models.CharField(max_length=500, null=True, verbose_name='Nombre Comercial')),
                ('CorreoElectronico', models.CharField(max_length=200, verbose_name='Email')),
                ('Numero', models.BigIntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Numero de Identificación')),
                ('Tipo', models.IntegerField(verbose_name='Tipo de Identificación')),
                ('Provincia', models.CharField(max_length=200, null=True, verbose_name='Provincia')),
                ('Canton', models.CharField(max_length=200, null=True, verbose_name='Cantón')),
                ('Distrito', models.CharField(max_length=200, null=True, verbose_name='Distrito')),
                ('Barrio', models.CharField(max_length=200, null=True, verbose_name='Barrio')),
                ('OtrasSenas', models.CharField(max_length=400, null=True, verbose_name='Otras señas')),
                ('CodigoPais', models.IntegerField(null=True, verbose_name='Código País')),
                ('NumTelefono', models.CharField(max_length=20, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Emisor',
                'verbose_name_plural': 'Emisores',
                'ordering': ['Nombre'],
            },
        ),
        migrations.CreateModel(
            name='Resumen',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('CodigoMoneda', models.CharField(max_length=64, verbose_name='Código moneda')),
                ('TipoCambio', models.FloatField(verbose_name='Tipo de cambio')),
                ('TotalServGravados', models.FloatField(null=True, verbose_name='Total servicios gravados')),
                ('TotalServExentos', models.FloatField(null=True, verbose_name='Total servicios exentos')),
                ('TotalServExonerado', models.FloatField(null=True, verbose_name='Total servicios exonerados')),
                ('TotalMercanciasGravadas', models.FloatField(null=True, verbose_name='Total mercancias gravadas')),
                ('TotalMercanciasExentas', models.FloatField(null=True, verbose_name='Total mercancias exentas')),
                ('TotalMercExonerada', models.FloatField(null=True, verbose_name='Total mercancias exoneradas')),
                ('TotalGravado', models.FloatField(null=True, verbose_name='Total gravado')),
                ('TotalExento', models.FloatField(null=True, verbose_name='Total exento')),
                ('TotalExonerado', models.FloatField(null=True, verbose_name='Total exonerado')),
                ('TotalVenta', models.FloatField(verbose_name='Total venta')),
                ('TotalDescuentos', models.FloatField(null=True, verbose_name='Total descuento')),
                ('TotalVentaNeta', models.FloatField(verbose_name='Total venta neta')),
                ('TotalImpuesto', models.FloatField(verbose_name='Total impuesto')),
                ('TotalIVADevuelto', models.FloatField(verbose_name='Total IVA Devuelto')),
                ('TotalOtrosCargos', models.FloatField(null=True, verbose_name='Total otros cargos')),
                ('TotalComprobante', models.FloatField(verbose_name='Total comprobante')),
            ],
            options={
                'verbose_name': 'Resumen',
                'verbose_name_plural': 'Resumenes',
            },
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('Clave', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Clave')),
                ('CodigoActividad', models.IntegerField(null=True, verbose_name='Código de actividad')),
                ('NumeroConsecutivo', models.BigIntegerField(null=True, verbose_name='Número de consecutivo')),
                ('FechaEmision', models.DateTimeField(verbose_name='Fecha de emisión')),
                ('CondicionVenta', models.IntegerField(null=True, verbose_name='Condición de venta')),
                ('MedioPago', models.IntegerField(null=True, verbose_name='Medio de pago')),
                ('detalle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documento.detalle')),
                ('emisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documento.emisor')),
                ('resumen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documento.resumen')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]
