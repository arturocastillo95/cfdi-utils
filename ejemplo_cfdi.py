from cfdi_utils import CFDI40
from cfdi_utils.SelloDigital import SelloDigital
import zeep


from io import StringIO
from datetime import datetime
from pathlib import Path
import lxml.etree as ET

PATH_CER = Path('support-files/CSD_XOJI740919U48_20190528180358/30001000000400002330.cer')
PATH_KEY = Path('support-files/CSD_XOJI740919U48_20190528180358/CSD_INDRID_XODAR_JIMENEZ_XOJI740919U48_20190528_180344.key')
CONTRASEÑA = '12345678a'


def timbrar_cfdi(usr, password, cfdi_sellado):
    """
    Timbra un CFDI sellado
    """
    client = zeep.Client(wsdl='http://dev33.facturacfdi.mx/WSTimbradoCFDIService?wsdl')
    try:
        accesos_type = client.get_type('ns1:accesos')
        accesos = accesos_type(usuario=usr, password=password)
        cfdi_timbrado = client.service.TimbrarCFDI(accesos=accesos, comprobante=cfdi_sellado.decode('utf-8'))
        return cfdi_timbrado
    except zeep.exceptions.Fault as e:
        print(e)
        return None



# Crear un objeto SelloDigital con el certificado y la llave privada
sello = SelloDigital(PATH_CER, PATH_KEY, CONTRASEÑA)
comprobante_dict = {}

CFDI_COMPROBANTE = {
    'Version': '4.0',
    'FormaPago': '01',
    'NoCertificado': sello.numero_cer,
    'Certificado': sello.cert_base64,
    'SubTotal': 100.00,
    'Total': 100.00,
    'Moneda': 'MXN',
    'TipoDeComprobante': 'I',
    'MetodoPago': 'PUE',
    'LugarExpedicion': '44970',
    # 'Sello': 'faltante',
    'Fecha': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    'Exportacion': '01',
    'Descuento': 1.00,
}

CFDI_EMISOR = {
    'Rfc': 'XOJI740919U48',
    'Nombre': 'INGRID XODAR JIMENEZ',
    'RegimenFiscal': '612',
}

CFDI_RECEPTOR = {
    'Rfc': 'XAXX010101000',
    'Nombre': 'Publico en General',
    'UsoCFDI': 'G01',
    'DomicilioFiscalReceptor' : '78090',
    'RegimenFiscalReceptor': '601',
}

CFDI_CONCEPTOS = [{
    'ClaveProdServ': '10101502',
    'NoIdentificacion': '1',
    'Cantidad': 1.000000,
    'ClaveUnidad': 'B17',
    'Unidad': 'Actividad',
    'Descripcion': 'Pago',
    'ValorUnitario': 100.00,
    'Importe': 100.00,
    'ObjetoImp': '02',
    'Impuestos': {
        'Traslados': [{
            'Base': '100.00',
            'Impuesto': '002',
            'TipoFactor': 'Tasa',
            'TasaOCuota': '0.160000',
            'Importe': '16.00',
    }]},
}]

comprobante_dict['Emisor'] = CFDI40.EmisorType(**CFDI_EMISOR)
comprobante_dict['Receptor'] = CFDI40.ReceptorType(**CFDI_RECEPTOR)

conceptos_obj = CFDI40.ConceptosType()

# Agregar conceptos al comprobante con impuestos
for concepto in CFDI_CONCEPTOS:
    
    concepto_impuesto = concepto.pop('Impuestos') if 'Impuestos' in concepto else None

    if concepto_impuesto:
        traslados = concepto_impuesto.pop('Traslados')
        traslado_obj = CFDI40.TrasladosType()

        for traslado in traslados:
            traslado_obj.Traslado.append(CFDI40.TrasladoType(**traslado))

        concepto['Impuestos'] = CFDI40.ImpuestosType(Traslados=traslado_obj)
    
    conceptos_obj.add_Concepto(CFDI40.ConceptoType(**concepto))

comprobante_dict['Conceptos'] = conceptos_obj

#Creamos el objeto comprobante
cfdi_obj = CFDI40.Comprobante(**comprobante_dict, **CFDI_COMPROBANTE)

#Exportamos el comprobante sin sellar a XML
output = StringIO()
cfdi_obj.export(output, 0)

#Sellamos el comprobante
signed_xml = sello.sellar_xml_2(output.getvalue())

cfdi_timbrado = timbrar_cfdi('pruebasWS', 'pruebasWS', signed_xml)
print(cfdi_timbrado)

#Exportamos el XML
# with open('cfdi_sellado.xml', 'wb') as f:
#     f.write(signed_xml)



