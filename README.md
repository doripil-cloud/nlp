# Contador de Palabras y Caracteres

Una herramienta sencilla en Python con interfaz gráfica para seleccionar archivos de texto y obtener estadísticas básicas de su contenido (número de palabras, caracteres con espacios y caracteres sin espacios).

## Características

* **Selección visual de archivos:** Abre una ventana del explorador de archivos utilizando `tkinter` para elegir archivos (`.txt`, `.csv`, o cualquier formato).
* **Conteo de caracteres:** Calcula el total de caracteres incluyendo y excluyendo espacios en blanco.
* **Conteo de palabras:** Analiza el contenido y devuelve el total de palabras.
* **Diseño modular:** Separación de responsabilidades entre lectura de archivos, procesamiento de datos y ejecución principal.

## Estructura del Proyecto

```text
├── main.py         # Punto de entrada: coordina la selección, lectura y muestra resultados
├── lector.py       # Módulo con interfaz gráfica (Tkinter) para seleccionar y leer el archivo
└── procesar.py     # Módulo con la lógica para contar palabras
```

## Requisitos

* **Python 3.x**
* **Tkinter** (incluido por defecto en Python para Windows y macOS; en distribuciones basadas en Debian/Ubuntu puede requerir `sudo apt-get install python3-tk`).
* No requiere instalación de paquetes externos (`pip`).

## Uso

1. Clona este repositorio en tu equipo:
   ```bash
   git clone https://github.com
   cd tu-repositorio
   ```

2. Asegúrate de que los tres archivos (`main.py`, `lector.py` y `procesar.py`) estén en el mismo directorio y ejecuta:
   ```bash
   python main.py
   ```

3. Selecciona el archivo que deseas analizar en la ventana emergente.

4. Visualiza el resumen directamente en tu terminal:
   ```text
   Caracteres con espacios:  150
   Caracteres sin espacios:  125
   Palabras:  26
   ```

## Autor

* **poly** - *Desarrollo inicial*
