import procesar as p
from lector import seleccionar_archivo, leer_archivo

archivo = seleccionar_archivo()
texto = leer_archivo(archivo)
p.reporte(archivo, texto)



