
#estructura diccionario
#       ------------------

#Ref : numerico como str
#Servicio:  {vacio}
#Detalle: nombre del producto en data
#Cant: cantidad del producto en data, pero transformado en txt
#Precio: 0.00 en todos los productos
#Vr/unit valor unitario total.
#Vr/total  valor unitario * cantidad 
#Vr/iva: 0.00 en todos los productos
#Total+iva: Valor Unitario total
#%iva : 0.00
#Tiva: {vacio}
#ico: 0.00
#ref1: {vacio}


def procesarDatosComoSys(data):
    resultadosSys = []
    for producto in data:
        ref = producto['referencia']
        Detalle =  producto['detalle']
        Cantidad =  str(producto['Cantidad'])
        VrUnit = str(producto['unt + iva'])
        TotalConIva = str(producto['Total'])

        resultadoSys = {
            'Ref' : ref,
            'Detalle': Detalle,
            'Cant': Cantidad,
            'Vrunit': VrUnit,
            'Total': TotalConIva
        }
        resultadosSys.append(resultadoSys)

    return resultadosSys


    