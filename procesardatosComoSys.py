
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
        Servicio = None
        Detalle =  producto['detalle']
        Cantidad =  str(producto['Cantidad'])
        precio = '0.00'
        VrUnit = str(producto['unt + iva'])
        vrTotal =  str(producto['Total'])
        vrIva = '0.00'
        TotalConIva = str(producto['Total'])
        iva = '0.00'
        Tiva = None
        ico = '0.00'
        ref1 = None

        resultadoSys = {
            'Ref' : ref,
            'Servicio':  Servicio,
            'Detalle': Detalle,
            'Precio': precio,
            'Cant': Cantidad,
            'Vr/unit': VrUnit,
            'Vr/total': vrTotal,
            'Vr/iva': vrIva,
            'Total+iva': TotalConIva,
            '%iva' : iva,
            'Tiva': Tiva,
            'ico': ico,
            'ref1': ref1
        }
        resultadosSys.append(resultadoSys)

    return resultadosSys


    