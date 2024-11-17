

from extraerXmlInterno import getXmlInterno, getPorductos
from extraerProductos import extraer_productos
from calcularPrecio import calcularPrecios
from crearExcel import crearExcel
from abrirtxt import leerTxt
from canjearProductos import canjearProductos
from procesardatosComoSys import procesarDatosComoSys
from crearCSV import crearCSV

from compararProductos import compararProductos

import json

with open("factura.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()

xmlninterno = getXmlInterno(xml_data)

if (xmlninterno):

    productos = getPorductos(xmlninterno)

    productosFactura = extraer_productos(productos)
    
    productosPrecio = calcularPrecios(productosFactura)

    productosTxt = leerTxt()#debe devolver un diccionario en donde la clave es el codigo de barras
                            #y el resultado es otro diccionario con la referencia y el detalle

    resultados = canjearProductos(productosPrecio,productosTxt)

    resultadosSys = procesarDatosComoSys(resultados)

    compararProductos(productosPrecio,productosTxt)

    #crearExcel(resultadosSys,'resultados_')
    crearCSV(resultadosSys)
    #tablaFinal = canjearProductos(productosPrecio,productosTxt)
    
    #print(tablaFinal)
    

else:
    print('No se encontró la descripción.(xml interno)')