from collections import Counter
from limpieza import quitar_palabras_vacias, limpiar_texto,tokenizar

diccionario = {
    "excelente": 1.0, "bueno": 0.7, "genial": 0.9, "feliz": 0.8,
    "malo": -0.7, "pésimo": -1.0, "triste": -0.6, "error": -0.5,
    "lento": -0.4, "rápido": 0.5, "recomiendo": 0.8, "problema": -0.6
}

#
#   Analiza el diccionario de palabras unicas contra el diccionario de polaridad
#   para calcular un indice simlpe de sentimiento.
#   f = lista de palabras unicas en el archivo con su frecuencia
#
def analiza_polaridad(frec):
    polaridad=0
    for word in diccionario:
        if word in frec:
            print("Coincindencia:",word, diccionario[word], frec[word])
            polaridad+=(diccionario[word]*frec[word])/frec[word]
    if polaridad > 0:
        print("Polaridad positiva")
    elif polaridad < 0:
        print("Polaridad Negativa")
    else:
        print("Polaridad Neutral")
    print("Polaridad final igual a :", polaridad)
    
    return polaridad

def obtener_frecuencias(tokens):
    return(Counter(tokens))
    
def obtener_TTR(tokens):
    # 2. Calcular totales y únicos
    total_tokens = len(tokens)
    palabras_unicas = len(set(tokens))

    # 3. Calcular TTR (evitando división entre cero)
    ttr = palabras_unicas / total_tokens if total_tokens > 0 else 0

    print(f"Tokens totales: {total_tokens}")      
    print(f"Palabras únicas: {palabras_unicas}")  
    print(f"TTR: {ttr:.2f}")                      
    

def cuenta_palabras( texto ):
    # split() divide el texto por los espacios en blanco
    palabras = texto.split()
    return len(palabras)

def reporte(archivo, texto):
    print("Analisis del archivo: ", archivo)
    print()
    print("Caraceteres:","="*20)
    print("Totales:        ", len(texto))
    print("Sin especiales: ", len(limpiar_texto(texto)) )
    print()
    print("Palabras: ","="*20)
    print("Totales:        ", cuenta_palabras(texto))    
    tokens = quitar_palabras_vacias(tokenizar(texto))
    print("Sin stop/words: ", len(tokens))    
    f = obtener_frecuencias(tokens)
    print("Palabras sin stop/words más repetidas ",f.most_common(5))    
    analiza_polaridad(dict(f))    
    obtener_TTR(tokens)
