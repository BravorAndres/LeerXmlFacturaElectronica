#se crea excel a partir de los datos extraidos en el diccionario, 




from datetime import datetime
import pandas as pd



def crearExcel(data):
    try:
        fecha = datetime.now().strftime("%d-%m")  # Ejemplo: '29-10'
        nombre_archivo = f"productos_{fecha}.xlsx"
        if os.path.exists(nombre_archivo):
            os.remove(nombre_archivo)
    
        # Crear un DataFrame a partir del diccionario
        df = pd.DataFrame.from_dict(data)
        # Guardar el DataFrame en un archivo Excel
        df.to_excel(nombre_archivo, index=False)
        print("Archivo Excel generado exitosamente.")
    except:
        print('error al crear archivo excel')
