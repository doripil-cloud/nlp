from collections import Counter

def obtener_frecuencias(tokens):
    frecuencias = Counter(tokens)
    print(frecuencias.most_common(5))
    

def cuenta_palabras( texto ):
    # split() divide el texto por los espacios en blanco
    palabras = texto.split()
    return len(palabras)
