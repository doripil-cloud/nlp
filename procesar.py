#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:10:08 2026

@author: poly
"""

def cuenta_palabras( texto ):
    # split() divide el texto por los espacios en blanco
    palabras = texto.split()
    return len(palabras)