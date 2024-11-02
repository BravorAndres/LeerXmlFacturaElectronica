#extrae los productos del diccionario creado con el xml interno

# retora: descripcion, percent(iva), cantidad, codigo(id del producto, en ocaciones se corresponde con el codigo de barras),
# precio unitario antes de iva.




# Función para extraer los productos. Recibe el 
def extraer_productos(data):
    resultados = []
    for producto in data:
        # Usar get() para evitar errores si la clave no existe
        
        id_producto = producto.get('cbc:ID', 'N/A')
        descripcion = producto.get('cac:Item', {}).get('cbc:Description', 'N/A')
        cantidad = producto.get('cbc:InvoicedQuantity',{}).get('#text')

        try:
            percent = producto.get('cac:TaxTotal', {}).get('cac:TaxSubtotal', {}).get('cac:TaxCategory', {}).get('cbc:Percent', 'N/A')
        except:
            percent = 'N/A'
        
        try:
            codigo = producto.get('cac:Item').get('cac:StandardItemIdentification',{}).get('cbc:ID',{}).get('#text','N/A')
        except:
            codigo = 'N/A'

        precio = producto.get('cac:Price', {}).get('cbc:PriceAmount', {}).get('#text', 'N/A')
        # Guardar los datos extraídos en un diccionario
        resultado = {
            'Codigo': codigo,
           # 'ID': id_producto,
            'Descripción': descripcion,
            'cantidad': cantidad,
            'Percent': percent,
            'Precio': precio
        }
        resultados.append(resultado)
    
    return resultados