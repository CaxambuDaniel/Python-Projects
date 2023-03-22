# utils.py
import os

def gera_lista(comando, arquivo):
    os.system(comando)
    with open(arquivo) as f:
        lista = [line.strip('\n').strip() for line in f.readlines()]
    return lista