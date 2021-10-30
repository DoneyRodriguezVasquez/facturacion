from xml.etree  import ElementTree as ET  
from django.utils import timezone
from .models import Emisor, Detalle, Resumen, Factura 


class Facturas:
    errors = list()

    def __init__(self, xml_file, user):
        self.xml_file = xml_file
        self.user = user

        
    def validar(self):
        if not self.xml_file.name.endswith('.xml'):
            return False
        return True


    def handle_uploaded_file(self):
        emisor = dict()
        receptor = dict()
        detalle_fact = list()
        resumen_fact = dict()
        factura = dict()
        ns = {'def':'https://cdn.comprobanteselectronicos.go.cr/xml-schemas/v4.3/facturaElectronica'}
        tree = ET.parse(self.xml_file)
        root = tree.getroot()
        if root.tag.endswith('FacturaElectronica'):
            receptor = self.toDict(root, "def:Receptor", ns)
            
            if receptor['Numero'] != self.user.num_identificacion:
                self.errors.append('Error, no se puede cargar una factura con un número de identificación diferente al registrado.')
            else:
                for linea in root:
                    if linea.text is not None:
                        factura[linea.tag.replace('{'+ns['def']+'}','')] = linea.text
                
                emisor = self.toDict(root, "def:Emisor", ns)
                
                detalle_fact = self.obtiene_detalle(root, ns)

                resumen_fact = self.obtiene_resumen(root, ns)

                e = Emisor.objects.get_or_create(**emisor)
                d = Detalle.objects.create(**self.calculaIVA(detalle_fact))
                r = Resumen.objects.create(**resumen_fact)

                items = ['Clave','CodigoActividad','NumeroConsecutivo','FechaEmision','fecha_carga','CondicionVenta','MedioPago','emisor_id','owner_id','detalle_id','resumen_id']
                factura['emisor_id'] = e[0].Numero
                factura['detalle_id'] = d.id
                factura['resumen_id'] = r.id
                factura['fecha_carga'] = timezone.now()

                fact_copy = dict(factura)
                for item, val in fact_copy.items():
                    if item not in items:
                        del factura[item]
                print(factura)
                Factura.objects.get_or_create(**factura)
                """ try: 
                    Factura.objects.get_or_create(**factura) 
                except Exception :
                    for val in e:
                        print(val)
                    self.errors.append('Error, la factura ya existe.') """ 
                
        else:
            self.errors.append('Error, el documento cargado no es la factura')

    
    def toDict(self, root, string_tag, ns):
        diccionario = dict()
        for element in root.findall(string_tag,ns):
            for subelement in element:
                if subelement.text is not None:
                    diccionario[subelement.tag.replace('{'+ns['def']+'}','')] = subelement.text
                for linea in subelement:
                    if linea.text is not None:
                        diccionario[linea.tag.replace('{'+ns['def']+'}','')] = linea.text
        
        dic_copy = dict(diccionario)
        for key, val in dic_copy.items():
            if not(val.strip()):
                del diccionario[key]
            
        return diccionario


    def obtiene_detalle(self, root, ns):
        detalle_fact = list()
        linea_detalle = dict()
        linea_det = root.find("def:DetalleServicio",ns)

        for detalle in linea_det:
            for linea in detalle:
                if linea.text is not None:
                    linea_detalle[linea.tag.replace('{'+ns['def']+'}','')] = linea.text
                for imp in linea:
                    if imp.text is not None:
                        linea_detalle[linea.tag.replace('{'+ns['def']+'}','') + imp.tag.replace('{'+ns['def']+'}','')] = imp.text
            detalle_fact.append(linea_detalle)
            linea_detalle = dict()
        
        return detalle_fact


    def obtiene_resumen(self, root, ns):
        resumen_fact = dict()
        resumen = root.find("def:ResumenFactura",ns)
        items = ['CodigoMoneda','TipoCambio','TotalServGravados','TotalServExentos','TotalServExonerado','TotalMercanciasGravadas','TotalMercanciasExentas','TotalMercExonerada','TotalGravado','TotalExento','TotalExonerado','TotalVenta','TotalDescuentos','TotalVentaNeta','TotalImpuesto','TotalIVADevuelto','TotalOtrosCargos','TotalComprobante']       

        for linea in resumen:
            if linea.text is not None:
                resumen_fact[linea.tag.replace('{'+ns['def']+'}','')] = linea.text
            for moneda in linea:
                if moneda.text is not None:
                    resumen_fact[moneda.tag.replace('{'+ns['def']+'}','')] = moneda.text
        
        resumen = dict(resumen_fact)

        for item, val in resumen.items():
            if item not in items:
                del resumen_fact[item]
        for item in items:
            if item not in resumen:
                resumen_fact[item] = 0
        return resumen_fact


    def calculaIVA(self, detalle_factura):
        detalle = dict()
        iva13_bienes = 0
        iva13_servicios = 0
        iva4_bienes = 0
        iva4_servicios = 0
        iva2_bienes = 0
        iva2_servicios = 0
        iva1_bienes = 0
        iva1_servicios = 0
        subtotal_serv = 0
        subtotal_bienes = 0
        total_serv = 0 
        total_bienes = 0 
        SubTotal = 0
        ImpuestoNeto = 0
        MontoTotal = 0

        for linea in detalle_factura:

            if linea.get('UnidadMedida') in ['Os', 'Sp', 'Spe', 'St']:
                if linea.get('ImpuestoCodigo') != None:
                    if int(float(linea.get('ImpuestoTarifa'))) == 13:
                        iva13_servicios += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 4:
                        iva4_servicios += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 2:
                        iva2_servicios += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 1:
                        iva1_servicios += float(linea.get('ImpuestoMonto'))
                    subtotal_serv += float(linea.get('SubTotal'))
                    total_serv += float(linea.get('MontoTotalLinea'))

            else:
                  if linea.get('ImpuestoCodigo') != None:
                    if int(float(linea.get('ImpuestoTarifa'))) == 13:
                        iva13_bienes += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 4:
                        iva4_bienes += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 2:
                        iva2_bienes += float(linea.get('ImpuestoMonto'))
                    elif int(float(linea.get('ImpuestoTarifa'))) == 1:
                        iva1_bienes += float(linea.get('ImpuestoMonto'))
                    subtotal_bienes += float(linea.get('SubTotal'))
                    total_bienes += float(linea.get('MontoTotalLinea'))

            SubTotal += float(linea.get('SubTotal'))
            if linea.get('ImpuestoNeto') is not None: 
                ImpuestoNeto += float(linea.get('ImpuestoNeto')) 
            else: 
                ImpuestoNeto += 0
            MontoTotal = float(linea.get('MontoTotal'))  

        detalle['iva13_bienes'] = iva13_bienes
        detalle['iva13_servicios'] = iva13_servicios
        detalle['iva4_bienes'] = iva4_bienes
        detalle['iva4_servicios'] = iva4_servicios
        detalle['iva2_bienes'] = iva2_bienes
        detalle['iva2_servicios'] = iva2_servicios
        detalle['iva1_bienes'] = iva1_bienes
        detalle['iva1_servicios'] = iva1_servicios
        detalle['subtotal_bienes'] = subtotal_bienes
        detalle['subtotal_serv'] = subtotal_serv
        detalle['total_bienes'] = total_bienes
        detalle['total_serv'] = total_serv
        detalle['SubTotal'] = SubTotal
        detalle['ImpuestoNeto'] = ImpuestoNeto
        detalle['MontoTotal'] = MontoTotal

        return detalle