#extrae los productos del diccionario creado con el xml interno

# retora: descripcion, percent(iva), cantidad, codigo(id del producto, en ocaciones se corresponde con el codigo de barras),
# precio unitario antes de iva.




# Función para extraer los productos. Recibe el xml interno
def extraer_productos(data):
    resultados = []
    for producto in data:
        # Usar get() para evitar errores si la clave no existe
        
        id_producto = producto.get('cbc:ID', 'N/A')
        descripcion = producto.get('cac:Item', {}).get('cbc:Description', 'N/A')
        cantidad = producto.get('cbc:InvoicedQuantity',{}).get('#text')

        try:
            percent = producto.get('cac:TaxTotal', {}).get('cac:TaxSubtotal', {}).get('cac:TaxCategory', {}).get('cbc:Percent',0)
        except:
            percent = '0'
        
        try:
            codigo = producto.get('cac:Item').get('cac:StandardItemIdentification',{}).get('cbc:ID',{}).get('#text','N/A')
        except:
            codigo = 'error'
        try:
            descuento = producto.get('cac:AllowanceCharge', {}).get('cbc:MultiplierFactorNumeric')

        except:
            descuento = '0'

        precio = producto.get('cac:Price', {}).get('cbc:PriceAmount', {}).get('#text', 'N/A')
        # Guardar los datos extraídos en un diccionario
        resultado = {
            'codigo': codigo,
           # 'ID': id_producto,
            'descripción': descripcion,
            'cantidad': cantidad,
            'iva': percent,
            'precio': precio,
            'descuento': descuento
        }
        resultados.append(resultado)
    
    return resultados