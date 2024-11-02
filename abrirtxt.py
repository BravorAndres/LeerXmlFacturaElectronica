
def leerTxt():
    productos_txt = {}
    with open('productosTxt.txt', 'r', encoding='latin-1') as file:
        for line in file:
            # Limpiar línea y dividir en componentes
            line = line.strip()
            line = line.strip('\n')
            referencia, detalle, codigo = line.split('","')
        
            # Guardar el producto en el diccionario con el código como clave
            productos_txt[codigo.strip('"')] = {'referencia': referencia.strip('"'), 'detalle': detalle.strip('"')}
    return productos_txt
    #return productos_txt
