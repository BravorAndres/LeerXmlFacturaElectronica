
#  script para retornar el xml interno de la factura y los datos del xml Interno


import xmltodict
import json

with open("factura.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()

# Convertir XML a diccionario



# Función para encontrar la primera aparición de "cbc:Description" ( contiene el xml con los datos de la factura)
def encontrar_xml(diccionario):
    if isinstance(diccionario, dict):
        # Verificar si la clave "cbc:Description" está presente
        if "cbc:Description" in diccionario:
            return diccionario["cbc:Description"]
        # Si no, explorar recursivamente los valores
        for valor in diccionario.values():
            resultado = encontrar_xml(valor)
            if resultado:
                return resultado
    elif isinstance(diccionario, list):
        # Si es una lista, revisar cada elemento
        for elemento in diccionario:
            resultado = encontrar_xml(elemento)
            if resultado:
                return resultado
    return None  # Si no encuentra nada, devuelve None


def getXmlInterno(xmlOriginal):
    diccionario = xmltodict.parse(xmlOriginal)
    return encontrar_xml(diccionario)

def getPorductos(xmlinterno):
    diccionario2 = xmltodict.parse(xmlinterno)
    json_data2 = json.dumps(diccionario2, indent=4)
    productos = diccionario2.get('Invoice').get('cac:InvoiceLine')
    return productos