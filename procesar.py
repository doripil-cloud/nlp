from collections import Counter

def obtener_frecuencias(tokens):
    frecuencias = Counter(tokens)
    print("Palabras sin stop/words más repetidas ",frecuencias.most_common(5))
    
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
