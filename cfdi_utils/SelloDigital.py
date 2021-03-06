from pathlib import Path
import ssl
import base64
from M2Crypto import X509
import lxml.etree as ET

from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import PKCS1_v1_5


CURRENT_PATH = Path(__file__).parent
DEFAULT_CADENA_ORIGINAL = CURRENT_PATH / 'xslt/cadenaoriginal_4_0.xslt'

class SelloDigital():
    def __init__(self, path_cer, path_key, password):
        self.path_cer = path_cer
        self.path_key = path_key
        self.password = password
        self.cert_file = open(self.path_cer, 'rb').read()
        self.valido_desde = None
        self.valido_hasta = None

    @property
    def path_cer(self):
        return self._path_cer
    
    @path_cer.setter
    def path_cer(self, value):
        if not isinstance(value, Path) or not value.exists():
            raise FileNotFoundError('El archivo {} no existe'.format(value))
        self._path_cer = value
    
    @property
    def path_key(self):
        return self._path_key

    @path_key.setter
    def path_key(self, value):
        if not Path(value).exists():
            raise FileNotFoundError('El archivo {} no existe'.format(value))
        self._path_key = value

    @property
    def cert(self):
        return (ssl.DER_cert_to_PEM_cert(self.cert_file)).encode()

    @property
    def key(self):
        pem_key = RSA.import_key(open(str(self.path_key), 'rb').read(), self.password)
        return pem_key

    @property
    def numero_cer(self):
        obj_cer = X509.load_cert_string(self.cert)
        tNumero = hex(obj_cer.get_serial_number()).split('x')[1] 
        rNumero = tNumero2 = ''

        for i in range(1, len(tNumero), 2):
            tNumero2 = tNumero[0:i+1]
            rNumero = rNumero + tNumero2[-1]
    
        return rNumero

    @property
    def cert_base64(self):
        cert = open(self.path_cer, 'rb').read()
        return base64.b64encode(cert).decode('utf-8')

    # def validar_cer_key(self):
    #     obj_cer = X509.load_cert_string(self.cert)
    #     obj_key = RSA.load_key_string(self.key)
    #     return True if obj_key.check_key() > 0 else False

    def sellar_xml(self, xml_str, cadena_original_xslt=DEFAULT_CADENA_ORIGINAL):
        xdoc = ET.fromstring(xml_str)
        transformador = ET.XSLT(ET.parse(str(cadena_original_xslt)))
        cadena_original = transformador(xdoc)

        digest = SHA256.new()
        digest.update(str(cadena_original).encode('utf-8'))

        private_key = self.key
        signer = PKCS1_v1_5.new(private_key)
        sig = signer.sign(digest)
        signature = base64.b64encode(sig).decode('utf-8')

        xdoc.attrib['Sello'] = signature

        #Add schemaLocation attribute
        attr_qname = ET.QName('http://www.w3.org/2001/XMLSchema-instance', 'schemaLocation')
        attr_value = 'http://www.sat.gob.mx/cfd/4 http://www.sat.gob.mx/sitio_internet/cfd/4/cfdv40.xsd'
        xdoc.attrib[attr_qname] = attr_value

        return ET.tostring(xdoc, encoding='utf-8', method='xml', pretty_print=True)

def main():
    pass

if __name__ == '__main__':
    main()