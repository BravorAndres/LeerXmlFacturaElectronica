

def procesarLinea(line):
    line = line.strip()
    line = line.strip('\n')
    referencia, detalle, codigo = line.split('","')
    referencia = referencia.strip('"')
    codigo = codigo.strip('"')
    codigo, precioU = codigo.split(',')
    codigo = codigo.strip('"')
    detalle = detalle.strip('"')

    return codigo,referencia,detalle,precioU


def leerTxt():
    productos = {}
    with open('productosTxt.txt', 'r', encoding='latin-1') as file:
        for line in file:
            codigo,referencia,detalle,precioU = procesarLinea(line)
            productos[codigo] = {'referencia':referencia, 'detalle':detalle,'precio':precioU}
    return productos

