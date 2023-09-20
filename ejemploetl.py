import pandas as pd

archivo_origen = "g1etl\data.csv"

# Leer los datos desde el archivo CSV y especificar que la primera fila es el encabezado
datos = pd.read_csv(archivo_origen, delimiter=';', header=0)

# Verificar los primeros registros
print(datos.head())
print(datos.columns)

# Agregar una nueva columna 'suma' que contenga la suma de dos columnas existentes
# Asumiendo que las columnas se llaman 'columna1' y 'columna2' en tu archivo CSV
datos['suma'] = datos['columna1'] + datos['columna2']
datos['resta'] = datos['columna1'] - datos['columna2']
datos['multiplicacion'] = datos['columna1'] * datos['columna2']

# Crear una nueva columna 'es_par' utilizando un bucle for
datos['es_par'] = ""

for index, row in datos.iterrows():
    print("index", index)
    print("row", row)
    if row['multiplicacion'] % 2 == 0:
        datos.at[index, 'es_par'] = 'par'
    else:
        datos.at[index, 'es_par'] = 'impar'

# Verificar los cambios
print(datos)

# Ruta al archivo CSV de destino
archivo_destino = "datos_transformados.csv"

# Guardar los datos transformados en un nuevo archivo CSV
datos.to_csv(archivo_destino, index=False)

# Verificar que se haya guardado correctamente
print(f"Los datos transformados se han guardado en {archivo_destino}")
