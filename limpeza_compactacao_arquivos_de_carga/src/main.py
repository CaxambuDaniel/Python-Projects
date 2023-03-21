#!/usr/bin/env python3
#_*_ coding: utf-8 _*_
#----------------------------------------------------------------------------
#Created By: Daniel Carvalho de Souza (Caxambu)
#Created Date: 16/01/2023
#Last Update: 21/03/2023
# Version: '1.0'
#----------------------------------------------------------------------------
""" Criado para realizar a limpeza e compactação dos arquivos de carga da solução autorize """
#----------------------------------------------------------------------------
#imports
#----------------------------------------------------------------------------
import os
import subprocess
import string
import logging
#----------------------------------------------------------------------------
#Criando e  configurando logger
#----------------------------------------------------------------------------
logging.basicConfig(filename="/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/log/limpeza_compactacao_carga.log",
                    format="%(levelname)s %(asctime)s - %(message)s",
                    filemode='a')
#Criando um logger                    
logger = logging.getLogger()

#setando o threshold de logger para DEBUG
logger.setLevel(logging.DEBUG)
#----------------------------------------------------------------------------
#Funcoes
#----------------------------------------------------------------------------
def gera_lista(comando,arquivo):
    os.system(comando)
    abre_arquivo = open(arquivo)
    geralista = abre_arquivo.readlines()
    lista =[line.strip('\n').strip() for line in geralista]
    return lista

def gera_lista_clientes():
    lista_clientes = gera_lista("ls -h /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/ > /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/clientes.txt","/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/clientes.txt") 
    return lista_clientes


gera_lista_clientes()
    

 