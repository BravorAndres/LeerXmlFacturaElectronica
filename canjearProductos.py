
from crearExcel import crearExcel

def canjearProductos(data,txt):
    
    resultados = []
    fallidos = []
    print('priductos del xml: ',len(data),'\n===================')
    
    for producto in data:
        codigo = producto.get('Codigo')


        
        if codigo in txt.keys():
            productoTxt = txt[codigo]
            # Crear el resultado combinado
           
            resultado = {
                'referencia': productoTxt['referencia'],
                'detalle': productoTxt['detalle'],
                'Cantidad': producto['Cantidad'],
                'unt + iva': producto['unt + iva'],
                'Total': producto['Total'],
               # 'nombre':producto['Descripcion']
            }
            resultados.append(resultado)
            
        else:
            fallidos.append(producto)


    print('\n=====================\nproductos canjeados: ',len(resultados),'\n')
    crearExcel(fallidos,'fallidos_')
    return resultados