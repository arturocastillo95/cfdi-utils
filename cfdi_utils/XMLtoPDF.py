from pathlib import Path
from Numero_a_Letras import numero_a_moneda
import base64

from io import BytesIO, StringIO
import lxml.etree as ET

from jinja2 import Template
from weasyprint import HTML, CSS
import qrcode
import qrcode.image.svg

#Import CFDI40 from the same directory
import sys
sys.path.append('.')
import CFDI40

EXAMPLE_XML             = Path('cfdi4_generico.xml')
RUNNING_PATH            = Path(__file__).parent
CFDI_HTML               = RUNNING_PATH / Path('templates/cfdi_sencillo.html')
CFDI_CSS                = RUNNING_PATH / Path('templates/cfdi_sencillo.css')
CADENA_ORIGINAL_TIMBRE  = RUNNING_PATH / Path('xslt/cadenaoriginal_TFD_1_1.xslt')

def qr_url(comprobante):
    base_url = 'https://verificacfdi.facturaelectronica.sat.gob.mx/default.aspx'
    qr_url = '%s?id=%s' % (base_url, comprobante.Complemento.TimbreFiscalDigital.UUID)
    qr_url = '%s&re=%s' % (qr_url, comprobante.Emisor.Rfc)
    qr_url = '%s&rr=%s' % (qr_url, comprobante.Receptor.Rfc)
    qr_url = '%s&tt=%s' % (qr_url, comprobante.Total)
    qr_url = '%s&fe=%s' % (qr_url, comprobante.Sello[-8:])
    base_qr = qr_url.encode('utf-8')
    return base_qr

def create_qr_svg(comprobante):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_url(comprobante))
    qr.make(fit=True)
    img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
    stream = BytesIO()
    img.save(stream)
    qr_svg = stream.getvalue()
    qr_svg = qr_svg.decode('utf-8')
    #Remove the XML header
    qr_svg = qr_svg.replace('<?xml version="1.0" encoding="UTF-8"?>', '')
    return qr_svg

def get_cadena_original_timbre(timbre_xml, xslt_cadena_timbre):
    xdoc = ET.fromstring(timbre_xml)
    transformador = ET.XSLT(ET.parse(str(xslt_cadena_timbre)))
    cadena_original = transformador(xdoc)
    return str(cadena_original).encode('utf-8')

def get_timbre_xml(comprobante):
    bstring = str(comprobante.Complemento.TimbreFiscalDigital).encode('utf-8')
    string = bstring.decode('utf-8')
    #Add xmlns to the root element
    string = string.replace('<tfd:TimbreFiscalDigital', '<TimbreFiscalDigital xmlns="http://www.sat.gob.mx/TimbreFiscalDigital"')
    return bytes(string, 'utf-8')

def xml_to_pdf(xml_file, xslt_cadena_timbre=CADENA_ORIGINAL_TIMBRE ,html_file=CFDI_HTML, css_file=CFDI_CSS, output_file=None):
    try:
        comprobante = CFDI40.Comprobante.from_xml(xml_file)
    except Exception as e:
        raise Exception('Error al leer el archivo xml: %s' % e)
    try:
        timbre_xml = get_timbre_xml(comprobante)
    except Exception as e:
        print(e)
        raise Exception('No se encontró el timbre fiscal digital')
    try:
        cadena_original = get_cadena_original_timbre(timbre_xml, xslt_cadena_timbre)
    except Exception as e:
        print(e)
        raise Exception('No se encontró la cadena original del timbre fiscal digital')
    qr_svg = create_qr_svg(comprobante)
    total_en_letras = numero_a_moneda(comprobante.Total) + ' M.N'
    #Create the template
    template = Template(html_file.read_text())
    #Render the template
    html = template.render(
        cfdi=comprobante,
        cadena_original_timbre=cadena_original,
        qr_svg=qr_svg,
        numero_a_moneda=numero_a_moneda,
        total_en_letras=total_en_letras
    )
    #Create the PDF
    pdf = HTML(string=html).write_pdf(output_file, stylesheets=[CSS(string=css_file.read_text())])

def main():
    xml_to_pdf(EXAMPLE_XML, output_file=RUNNING_PATH / Path('cfdi_timbrado.pdf'))

if __name__ == '__main__':
    main()
