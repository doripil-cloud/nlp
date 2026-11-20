import tkinter as tk
from tkinter import filedialog

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    ruta_archivo = filedialog.askopenfilename(
        title="Selecciona un archivo",
        filetypes=[
            ("Todos los archivos", "*.*"),
            ("Archivos de texto", "*.txt"),
            ("Archivos CSV", "*.csv"),
        ]
    )
    root.update()
    root.destroy()
    
    return ruta_archivo

def leer_archivo( archivo ):
    with open(archivo, "r") as file:
        texto = file.read()
        
    return(texto)


if __name__ == "__main__":
    archivo = seleccionar_archivo()
    texto = leer_archivo(archivo)
    print(texto[:1000])