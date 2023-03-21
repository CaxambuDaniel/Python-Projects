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

def checa_qtd_diretorios(cliente):
    ano_atual = datetime.now().strftime("%Y")
    qtd_dir = int(subprocess.check_output(f"ls -hd /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{ano_atual}*/ | wc -l", shell = True))    
    if  qtd_dir >  2:
        lista_qtd_dir = gera_lista(f"find /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/`date +%Y`* -type d  -mtime -365 -ls| rev | cut -d'-' -f 1 | rev > /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/qtd_dir.txt","/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/qtd_dir.txt")       
        print(lista_qtd_dir)
        deleta_dir_min(cliente,lista_qtd_dir) 

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

def deleta_dir_min(cliente,lista_qtd_dir):    
    if lista_qtd_dir:
        os.system(f"rm -r /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/*{min(lista_qtd_dir)}")
    else:
        print(f"Lista vazia para o cliente {cliente}")



lista_clientes = gera_lista_clientes()
compacta_arquivos_carga(lista_clientes)
gera_lista_qtd_dir(lista_clientes)

    

    