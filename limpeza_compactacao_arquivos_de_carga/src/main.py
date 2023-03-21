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
from datetime import datetime, timedelta
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

def gera_lista_qtd_dir(lista_clientes):
    for cliente in lista_clientes:
        checa_qtd_diretorios(cliente) 



def compacta_arquivos_carga(lista_clientes):
    for cliente in lista_clientes:
        data_ontem = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        
        dir_ontem = f"/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{data_ontem}"
        dir_hoje = f"/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{data_hoje}"
        
        if os.path.exists(dir_ontem):
            os.system(f"find {dir_ontem} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")
            os.system(f"find {dir_hoje} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")
        else:
            os.system(f"find {dir_hoje} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")




lista_clientes = gera_lista_clientes()
compacta_arquivos_carga(lista_clientes)

    

 