

def calcularPrecios(data):
    
    resultados = []
    try:
        for producto in data:

            cantidad = float(producto.get('cantidad', '0') or 0)
            precio = float(producto.get('precio', '0'))
            descuento = float(producto.get('descuento', '0')or 0)
            iva = float(producto.get('iva', '0') or 0)
        
            #print(' ',cantidad,' ',precio,' ',descuento,' ',iva,'\n')

            # Calcular el precio después del descuento
            precio_con_descuento = precio * (1 - descuento / 100)

            # Aplicar el IVA si existe
            precio_con_iva = precio_con_descuento * (1 + iva / 100) if iva else precio_con_descuento

            # Calcular el total multiplicando por la cantidad
            total = precio_con_iva * cantidad

            # Agregar los datos procesados al resultado
            resultados.append({
                'Codigo': producto.get('codigo'),
                'Descripción': producto.get('descripción'),
                'Cantidad': cantidad,
                'unt + iva': round(precio_con_iva, 2),
                'Total': round(total, 2)
            })
    except ValueError as e:
        print(f"Error en los datos del producto: {producto['codigo']}",e)
    return resultados