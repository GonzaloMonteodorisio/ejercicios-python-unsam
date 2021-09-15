# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 22:34:45 2021

@author: Marian
"""

def buscar_precio(elemento):
    with open('../Data/precios.csv', 'rt', encoding = "utf8") as f:
        fruta_esta = False
        for line in f:
            fruta = line.split(",")
            if elemento == fruta[0]: 
                fruta_esta = True
                print(f'El costo de {elemento} es {fruta[1]}')
                break
        if not fruta_esta:
            print('La fruta consultada no está en la lista')
              

fruta_a_consultar = input('Ingrese una fruta o verdura para conocer su precio: ')
buscar_precio(fruta_a_consultar)
                   