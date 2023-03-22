import os

def gera_lista(comando, arquivo):
    os.system(comando)
    abre_arquivo = open(arquivo)
    geralista = abre_arquivo.readlines()
    lista =[line.strip('\n').strip() for line in geralista]
    return lista
