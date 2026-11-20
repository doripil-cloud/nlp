palabras_vacias = {"el", "la", "los", "las", "un", "una", "unos", "unas", "lo", "al", "del", "a", "ante", "bajo", "cabe", "con", "contra", "de", "desde", "durante", "en", "entre", "hacia", "hasta", "mediante", "para", "por", "según", "sin", "so", "sobre", "tras", "versus", "y", "e", "ni", "o", "u", "pero", "mas", "sino", "aunque", "porque", "pues", "si", "que", "como", "cuando", "mientras", "donde", "ya", "ora", "yo", "tú", "él", "ella", "ello", "nosotros", "nosotras", "vosotros", "vosotras", "ellos", "ellas", "usted", "ustedes", "me", "te", "se", "nos", "os", "le", "les", "lo", "la", "los", "las", "mi", "mis", "mío", "mía", "míos", "mías", "tu", "tus", "tuyo", "tuya", "suyo", "suya", "sus", "nuestro", "nuestra", "nuestros", "nuestras", "vuestro", "vuestra", "este", "esta", "estos", "estas", "ese", "esa", "esos", "esas", "aquel", "aquella", "aquellos", "aquellas", "esto", "eso", "aquello", "aquí", "ahí", "allí", "allá", "acá", "ahora", "antes", "después", "luego", "hoy", "ayer", "mañana", "siempre", "nunca", "jamás", "también", "tampoco", "muy", "mucho", "poco", "bastante", "demasiado", "más", "menos", "casi", "solo", "solamente", "bien", "mal", "así", "entonces", "quizás", "quizá", "tal vez", "todavía", "aún", "ya", "no", "sí", "cada", "cualquier", "cualquiera", "cualquieras", "todo", "toda", "todos", "todas", "otro", "otra", "otros", "otras", "algún", "alguna", "algunos", "algunas", "ningún", "ninguna", "ningunos", "ningunas", "ambos", "ambas", "varios", "varias", "cierto", "cierta", "ciertos", "ciertas", "tanto", "tanta", "tantos", "tantas", "qué", "quién", "quiénes", "cuál", "cuáles", "cuánto", "cuánta", "cuántos", "cuántas", "cómo", "cuándo", "dónde", "adónde", "ser", "estar", "haber", "tener", "hacer", "poder", "deber", "querer", "ir", "dar", "decir", "soy", "eres", "es", "somos",  "son", "era", "eran", "fui", "fue", "han", "he", "hemos", "había", "has", "hay", "está", "están", "estaba", "tengo", "tiene", "tienen", "pueden", "hacer", "hace"}
signos = ".,;:!?¿¡\"'()[]{}-—…«»_*/\\"

def limpiar_texto(texto):
    texto =texto.lower()
    for signo in signos:
        texto = texto.replace(signo, " ")
    return texto

def tokenizar(texto):
    return limpiar_texto(texto).split()

def quitar_palabras_vacias(tokens):
    resultado = []
    for palabra in tokens:
        if palabra not in palabras_vacias:
            resultado.append(palabra)
        return resultado
        
