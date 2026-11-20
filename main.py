#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:52:45 2026

@author: poly
"""

from lector import seleccionar_archivo, leer_archivo
from procesar import cuenta_palabras

archivo = seleccionar_archivo()
texto = leer_archivo(archivo)

print("Caracteres con espacios: ", len(texto))
print("Caracteres sin espacios: ", len(texto.replace(" ", "")))
print("Palabras: ",cuenta_palabras(texto))
