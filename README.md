# Contador de Palabras y Caracteres

Una herramienta sencilla en Python con interfaz gráfica para seleccionar archivos de texto y obtener estadísticas básicas de su contenido (número de palabras, caracteres con espacios y caracteres sin espacios).

## Características

* **Selección visual de archivos:** Abre una ventana del explorador de archivos utilizando `tkinter` para elegir archivos (`.txt`, `.csv`, o cualquier formato).
* **Limpieza y tokenización** Eliminacion de espacios en blanco,  caracteres especiales y stop words.
* **Conteo de caracteres:** Calcula el total de caracteres incluyendo y excluyendo espacios en blanco.
* **Conteo de palabras:** Analiza el contenido y devuelve el total de palabras.
* **Estadísticas avanzadas:** Cálculo de frecuencia de palabras, cálculo de TTR(Token Type Ratio).
* **Diseño modular:** Separación de responsabilidades entre lectura de archivos, procesamiento de datos y ejecución principal.


## Estructura del Proyecto

```text
├── main.py         # Punto de entrada: coordina la selección, lectura y muestra resultados
├── lector.py       # Módulo con interfaz gráfica (Tkinter) para seleccionar y leer el archivo
├── procesar.py     # Módulo básico de contar palabras
└── limpieza.py     # Módulo para limpiar stop/words
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
    Analisis del archivo:  principito.txt
    
    Caraceteres: ====================
    Totales:         80391
    Sin especiales:  76286

    Palabras:  ====================
    Totales:         13129
    Sin stop/words:  6822
    Palabras sin stop/words más repetidas  [('principito', 203), ('dijo', 131), ('mãs', 75), ('rey', 61), ('planeta', 57)]
    Coincindencia: bueno 0.7 5
    Coincindencia: feliz 0.8 6
    Coincindencia: triste -0.6 8
    Polaridad positiva
    Polaridad final igual a : 0.9
    Tokens totales: 6822
    Palabras únicas: 2284
    TTR: 0.33

   ```
   





## Características

- **Conversión a minúsculas:** Hace que una misma palabra escrita de diferentes formas cuente como una sola. EJEMPLO: "Hola" y "hola".
- **Eliminación de signos de puntuación:** Reemplaza cada signo POR un espacio, para que si varias palabras están unidas por un signo de puntuación, las cuente como diferentes palabras. EJEMPLO: "hola,mundo" --> "hola mundo".
- **Tokenización:** Separa el texto que ya se limpio en una lista.
- **Filtrado de palabras vacias:** Elimina palabras que casi no aportan significado usando un `set`.

## Funciones

- **`limpiar_texto(texto):`** Pasa a minúsculas y quita los signos de puntuación.
- **`tokenizar(texto):`** Limpia el texto y devuelve una lista de palabras.
- **`quitar_palabras_vacias(tokens):`** Devuelve solo las palabras que no están en `palabras_vacias`.

## Uso

```python

texto = "Hoy fue un día excelente. ¡Me encanta programar!"

tokens = tokenizar(texto)
print(tokens)
# ['hoy', 'fue', 'un', 'día', 'excelente', 'me', 'encanta', 'programar']

utiles = quitar_palabras_vacias(tokens)
print(utiles)
# ['hoy', 'día', 'excelente', 'encanta', 'programar']
```

## Autores

- **Fernanda Narahi Rayas Flores** - 
- **Paulina Alejandra Ramirez Olmos** - 