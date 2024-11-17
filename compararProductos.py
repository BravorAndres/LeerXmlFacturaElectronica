from crearExcel import crearExcel


def compararPrecio(valor1, valor2, margen=100):
    """
    Compara dos valores con un margen permitido.

    Args:
        valor1 (float): Primer valor.
        valor2 (float): Segundo valor.
        margen (float): Margen dentro del cual los valores se consideran iguales.

    Returns:
        bool: True si la diferencia es mayor al margen, False en caso contrario.
    """
    # Calcular la diferencia absoluta entre los valores
    diferencia = abs(valor1 - valor2)
    
    # Comparar la diferencia con el margen
    if diferencia <= margen:
        return False  # Dentro del margen, se considera "igual"
    else:
        return True  # Fuera del margen, se considera "diferente"


def compararProductos(data, txt):
    cambiarPrecio = []
    for i in data:
        try:  # Esta línea está al mismo nivel que 'for'
            producto = txt[i.get('Codigo')]
            if(compararPrecio(float(producto.get('precio')),float(i.get('unt + iva')),100)):
                cambiarPrecio.append(i)
        except:  # Esta línea también está al mismo nivel que 'try'
            pass
    crearExcel(cambiarPrecio,"CambiarPrecios_")