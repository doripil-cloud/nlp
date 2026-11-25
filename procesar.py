from collections import Counter
from limpieza import quitar_palabras_vacias, limpiar_texto,tokenizar

diccionario = {
    "excelente": 1.0, "bueno": 0.7, "genial": 0.9, "feliz": 0.8,
    "malo": -0.7, "pésimo": -1.0, "triste": -0.6, "error": -0.5,
    "lento": -0.4, "rápido": 0.5, "recomiendo": 0.8, "problema": -0.6,
    "horrible": -1.0, "terrible": -1.0,
    "desagradable": -0.8, "frustrante": -0.8,
    "frustración": -0.8, "frustrado": -0.8, "frustrada": -0.8, "decepcionante": -0.9,
    "decepción": -0.9, "decepcionado": -0.8, "decepcionada": -0.8,
    "aburrido": -0.6, "aburrida": -0.6, "aburrimiento": -0.6,
    "difícil": -0.5, "complicado": -0.6, "complicada": -0.6,
    "confuso": -0.6, "confusa": -0.6, "confusión": -0.6,
    "defectuoso": -0.8, "defectuosa": -0.8, "defecto": -0.7, "fallido": -0.8, "fallida": -0.8,
    "odio": -1.0, "odiar": -1.0, "odiado": -1.0, "odiada": -1.0,
    "miedo": -0.7, "temor": -0.7, "preocupación": -0.6, "preocupado": -0.6, "preocupada": -0.6,
    "injusto": -0.8, "injusta": -0.8, "injusticia": -0.9, "fracaso": -1.0, "fracasado": -0.9,
    "fracasada": -0.9, "daño": -0.8, "dañado": -0.8, "dañada": -0.8, "perder": -0.6,
    "perdido": -0.6, "perdida": -0.6, "romper": -0.6, "roto": -0.7, "rota": -0.7, "caro": -0.4,
    "cara": -0.4, "insuficiente": -0.6, "deficiente": -0.7, "peligroso": -0.9, "peligrosa": -0.9,
    "desastre": -1.0, "desastroso": -1.0, "desastrosa": -1.0, "lamentable": -0.9,
    "terriblemente": -1.0, "negativo": -0.8, "negativa": -0.8,
    "pesadilla": -1.0, "asco": -1.0, "asqueroso": -1.0, "asquerosa": -1.0,
    "repugnante": -1.0, "molesto": -0.7, "molesta": -0.7, "molestia": -0.6,
    "molestar": -0.6, "irritante": -0.7, "irritación": -0.7, "irritado": -0.7, "irritada": -0.7,
    "enojado": -0.8, "enojada": -0.8, "enojo": -0.8, "enfado": -0.8, "furioso": -0.9, "furiosa": -0.9,
    "rabia": -0.9, "miserable": -1.0, "miseria": -0.9, "pobre": -0.4, "pobreza": -0.7, "debilidad": -0.6,
    "débil": -0.6, "desesperante": -0.9, "desesperación": -0.9, "desesperado": -0.8, "desesperada": -0.8,
    "angustia": -0.8, "angustiado": -0.8, "angustiada": -0.8, "tristeza": -0.8, "soledad": -0.7,
    "solitario": -0.6, "solitaria": -0.6, "insatisfecho": -0.8, "insatisfecha": -0.8, "insatisfacción": -0.8,
    "incorrecto": -0.7, "incorrecta": -0.7, "equivocado": -0.7, "equivocada": -0.7,
    "fallar": -0.7, "falló": -0.7, "fallando": -0.7, "perjudicial": -0.8,
    "dañino": -0.8, "dañina": -0.8, "costoso": -0.5, "costosa": -0.5, "carísimo": -0.6, "carísima": -0.6,
    "incómodo": -0.7, "incómoda": -0.7, "desordenado": -0.5,
    "desordenada": -0.5, "desorganizado": -0.6, "desorganizada": -0.6, "ineficiente": -0.8,
    "insatisfactorio": -0.8, "insatisfactoria": -0.8, "mediocre": -0.7,
    "vergonzoso": -0.8, "vergonzosa": -0.8, "vergüenza": -0.7, "culpa": -0.5,
    "culpable": -0.6, "mentira": -0.9, "mentiroso": -0.9, "mentirosa": -0.9,
    "falso": -0.7, "falsa": -0.7, "engaño": -0.9, "engañoso": -0.8,
    "engañosa": -0.8, "estafa": -1.0, "estafado": -0.9, "estafada": -0.9, "pérdida": -0.7,
    "retraso": -0.5, "retrasado": -0.5, "retrasada": -0.5,
    "insensible": -0.7, "egoísta": -0.8, "egoísmo": -0.8, "arrogante": -0.7, "arrogancia": -0.7,
    "grosero": -0.8, "grosera": -0.8, "irresponsable": -0.8, "irresponsabilidad": -0.8, "deshonesto": -0.9,
    "deshonesta": -0.9, "deshonestidad": -0.9,
    "maravilloso": 1.0, "maravillosa": 1.0,
    "increíble": 0.9, "perfecto": 1.0, "perfecta": 1.0,
    "hermoso": 0.9, "hermosa": 0.9,
    "precioso": 0.9, "preciosa": 0.9, "encantador": 0.9, "encantadora": 0.9, "encanta": 0.9,
    "encantan": 0.9, "encantó": 0.9, "agradable": 0.7, "divertido": 0.8,
    "divertida": 0.8, "satisfactorio": 0.8,
    "satisfactoria": 0.8, "interesante": 0.7, "útil": 0.7,
    "eficiente": 0.8, "amor": 1.0, "amoroso": 0.9,
    "amorosa": 0.9, "alegría": 0.9, "alegre": 0.8, "éxito": 1.0,
    "exitoso": 0.9, "exitosa": 0.9, "felicidad": 1.0, "confianza": 0.8, "confiable": 0.8,
    "disfrutar": 0.8, "disfruta": 0.8, "disfruté": 0.8, "agradecer": 0.8,
    "agradecido": 0.9, "agradecida": 0.9, "agradecimiento": 0.8, "mejorar": 0.7, "mejora": 0.7,
    "mejorado": 0.8, "mejorada": 0.8, "excelencia": 1.0, "extraordinario": 0.9,
    "extraordinaria": 0.9, "fantástico": 1.0, "fantástica": 1.0, "fabuloso": 0.9,
    "fabulosa": 0.9, "estupendo": 0.9, "estupenda": 0.9, "magnífico": 1.0, "magnífica": 1.0,
    "genialidad": 0.9, "brillante": 0.9, "amable": 0.8,
    "bondadoso": 0.9, "bondadosa": 0.9, "generoso": 0.8, "generosa": 0.8, "positivo": 0.8,
    "positiva": 0.8, "optimista": 0.8, "optimismo": 0.8,
    "esperanza": 0.8, "esperanzador": 0.8, "tranquilo": 0.7, "tranquila": 0.7,
    "diversión": 0.8, "placer": 0.8, "encanto": 0.8, "calidad": 0.8, "beneficio": 0.8,
    "beneficioso": 0.9, "beneficiosa": 0.9, "reconocimiento": 0.8, "admirable": 0.9,
    "admiración": 0.9, "recompensa": 0.8, "victoria": 1.0, "logro": 0.9,
    "creatividad": 0.8, "creativo": 0.8, "creativa": 0.8, "innovador": 0.9, "innovadora": 0.9,
    "excelentemente": 1.0, "amigable": 0.8, "amistoso": 0.8, "amistosa": 0.8, "favorable": 0.8,
    "recomendable": 0.8, "recomendado": 0.8, "recomendada": 0.8,
    "recomendaría": 0.8, "funciona": 0.6, "funcionó": 0.7, "funcionamiento": 0.6,
    "resuelto": 0.7, "resuelta": 0.7, "solución": 0.8, "solucionado": 0.8, "solucionada": 0.8,
    "cómodo": 0.8, "cómoda": 0.8,
    "rápidamente": 0.6, "seguro": 0.7, "segura": 0.7, "seguridad": 0.8, "paciencia": 0.7,
    "paciente": 0.7, "felizmente": 0.8, "maravilla": 0.9, "encantadoramente": 0.8,
    
}

#
#   Analiza el diccionario de palabras únicas contra el diccionario de polaridad
#   para calcular un indice simple de sentimiento.
#   f = lista de palabras únicas en el archivo con su frecuencia
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
