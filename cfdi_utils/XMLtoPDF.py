import lxml.etree as ET
from pathlib import Path
import CFDI40

EXAMPLE_XML = Path('cfdi_timbrado.xml')

# XML to CFDI object
cfdi = CFDI40.parse(EXAMPLE_XML)
print(cfdi.Complemento.TimbreFiscalDigital.FechaTimbrado)