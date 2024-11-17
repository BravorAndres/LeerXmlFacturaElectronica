import csv

def crearCSV(data):
    # Nombre del archivo CSV
    archivo_csv = "productos.csv"

    # Escribir la lista de diccionarios en el archivo CSV
    with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
        # Crear el escritor CSV
        escritor = csv.DictWriter(archivo, fieldnames=['Ref','Detalle','Cant','Vrunit','Total'])
    
        # Escribir los encabezados
        escritor.writeheader()
    
        # Escribir las filas
        escritor.writerows(data)


