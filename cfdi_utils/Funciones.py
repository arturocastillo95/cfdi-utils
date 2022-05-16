#Import CFDI40 from the same directory as this file
import sys
from io import StringIO
sys.path.append('.')
from cfdi_utils import CFDI40
from cfdi_utils.SelloDigital import SelloDigital

def procesar_conceptos(conceptos):
    """
    Convierte un diccionario de conceptos a un objeto ConcpetosType. Retorna el objeto ConceptosType y el objeto ImpuestosType10 (si existe).

    Tambien calcula y retorna el subtotal y el total de la factura.

    Retorna un diccionario con los conceptos, los impuestos (si existen), el subtotal y total de la factura.
    """
    conceptos_obj = CFDI40.ConceptosType()
    subtotal = 0

    #Creamos un objeto de impuestos para la clase padre Comprobante que tiene un hijo de tipo ImpuestosType10 el cual es un resumen de los impuestos
    resumen_impuestos = CFDI40.ImpuestosType10()
    resumen_traslados_obj = resumen_retenciones_obj = None
    result = {
        'Conceptos': None, 
        'Impuestos': None,
        'SubTotal': None,
        'Total': None
        }

    for concepto in conceptos:
        impuestos = concepto.pop('Impuestos') if 'Impuestos' in concepto else None

        if impuestos:
            #Creamos un objeto de impuestos para la clase Concepto
            concepto['Impuestos'] = CFDI40.ImpuestosType()
            traslados = impuestos.pop('Traslados') if 'Traslados' in impuestos else None
            retenciones = impuestos.pop('Retenciones') if 'Retenciones' in impuestos else None
            
            if traslados:
                resumen_traslados_obj = CFDI40.TrasladosType13() if not resumen_traslados_obj else resumen_traslados_obj
                traslados_obj = CFDI40.TrasladosType()
                for traslado in traslados:
                    traslados_obj.Traslado.append(CFDI40.TrasladoType(**traslado))
                    resumen_traslados_obj.Traslado.append(CFDI40.TrasladoType14(**traslado))
                    resumen_impuestos.TotalImpuestosTrasladados = traslado['Importe'] if not resumen_impuestos.TotalImpuestosTrasladados else resumen_impuestos.TotalImpuestosTrasladados + traslado['Importe']
                concepto['Impuestos'].Traslados = traslados_obj
            
            if retenciones:
                resumen_retenciones_obj = CFDI40.RetencionesType11() if not resumen_retenciones_obj else resumen_retenciones_obj
                retenciones_obj = CFDI40.RetencionesType()
                for retencion in retenciones:
                    retenciones_obj.Retencion.append(CFDI40.RetencionType(**retencion))
                    resumen_retenciones_obj.Retencion.append(CFDI40.RetencionType12(**retencion))
                    resumen_impuestos.TotalImpuestosRetenidos = retencion['Importe'] if not resumen_impuestos.TotalImpuestosRetenidos else resumen_impuestos.TotalImpuestosRetenidos + retencion['Importe']
                concepto['Impuestos'].Retenciones = retenciones_obj

        conceptos_obj.Concepto.append(CFDI40.ConceptoType(**concepto))
        subtotal += concepto['Importe']
    
    if resumen_traslados_obj or resumen_retenciones_obj:
        resumen_impuestos.Traslados = resumen_traslados_obj
        resumen_impuestos.Retenciones = resumen_retenciones_obj
        result['Impuestos'] = resumen_impuestos

        impuestos_trasladado = resumen_impuestos.TotalImpuestosTrasladados if resumen_impuestos.TotalImpuestosTrasladados else 0
        impuestos_retenido = resumen_impuestos.TotalImpuestosRetenidos if resumen_impuestos.TotalImpuestosRetenidos else 0
        result['Total'] = subtotal + impuestos_trasladado - impuestos_retenido
    else:
        result['Total'] = subtotal

    result['Conceptos'] = conceptos_obj
    result['SubTotal'] = subtotal
    return result

def dic_to_comprobante_obj(dic):
    """
    Convierte un diccionario a un objeto XML.
    """

    if not dic['Conceptos']:
        raise Exception('No hay conceptos en la factura')
    if not dic['Emisor']:
        raise Exception('No hay emisor en la factura')
    if not dic['Receptor']:
        raise Exception('No hay receptor en la factura')
    
    
    #Creamos un objeto de emisor
    dic['Emisor'] = CFDI40.EmisorType(**dic['Emisor'])
    #Creamos un objeto de receptor
    dic['Receptor'] = CFDI40.ReceptorType(**dic['Receptor'])

    #Procesamos los Conceptos e Impuestos para obtener un objeto de conceptos y un objeto de impuestos si existen
    conceptos_procesados = procesar_conceptos(dic['Conceptos'])
    dic['Conceptos'], dic['Impuestos'], dic['SubTotal'], dic['Total'] = conceptos_procesados['Conceptos'], conceptos_procesados['Impuestos'], conceptos_procesados['SubTotal'], conceptos_procesados['Total']

    #Creamos un objeto de comprobante
    comprobante = CFDI40.Comprobante(**dic)

    return comprobante

def generar_xml_sellado(dic, certificado=None, llave_privada=None, password=None):
    """
    Genera un XML a partir de un diccionario.
    """
    comprobante = dic_to_comprobante_obj(dic)

    #Creamos el XML sin sello
    xml = StringIO()
    comprobante.export(xml, 0)

    return xml.getvalue()

    # sello = SelloDigital(certificado, llave_privada, password)
    # xml_sellado = sello.sellar_xml(xml)
    
    # return xml_sellado
