#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:52:45 2026

@author: poly
"""

from lector import seleccionar_archivo, leer_archivo
from procesar import cuenta_palabras, obtener_frecuencias, obtener_TTR
from limpieza import limpiar_texto, tokenizar, quitar_palabras_vacias

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
    obtener_frecuencias(tokens)
    obtener_TTR(tokens)

archivo = seleccionar_archivo()
texto = leer_archivo(archivo)
reporte(archivo, texto)


