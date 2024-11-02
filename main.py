

from extraerXmlInterno import getXmlInterno, getPorductos
from extraerProductos import extraer_productos
from crearExcel import crearExcel

with open("factura.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()


xmlninterno = getXmlInterno(xml_data)

if (xmlninterno):
    porductos = getPorductos(xmlninterno)
    productosFactura = extraer_productos(porductos)
    crearExcel(productosFactura)
    
else:
    print('No se encontró la descripción.(xml interno)')