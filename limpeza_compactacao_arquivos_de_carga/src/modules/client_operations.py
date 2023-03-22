# client_operations.py
from modules.utils import gera_lista
from modules.logger_config import configure_logger 
import os
import subprocess
from datetime import datetime, timedelta

logger = configure_logger()

def gera_lista_clientes(logger):
    lista_clientes = gera_lista("ls -h /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/ > /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/clientes.txt","/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/clientes.txt") 
    logger.debug(f'Lista de clientes gerada: {lista_clientes}')
    return lista_clientes

def gera_lista_qtd_dir(lista_clientes, logger):
    for cliente in lista_clientes:
        logger.debug(f'Checando quantidade de diretórios para o cliente: {cliente}')
        checa_qtd_diretorios(cliente, logger) 

def checa_qtd_diretorios(cliente, logger):
    logger.debug(f"Checando quantidade de diretórios para o cliente: {cliente}")
    
    ano_atual = datetime.now().strftime("%Y")
    qtd_dir = int(subprocess.check_output(f"ls -hd /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{ano_atual}*/ | wc -l", shell = True))    
    
    if qtd_dir > 2:
        logger.info(f"Quantidade de diretórios maior que 2: {qtd_dir}")
        lista_qtd_dir = gera_lista(f"find /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/`date +%Y`* -type d -mtime -365 -ls| rev | cut -d'-' -f 1 | rev > /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/qtd_dir.txt", "/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/listas/qtd_dir.txt")
        
        logger.debug(f"Lista de diretórios gerada: {lista_qtd_dir}")
        
        print(lista_qtd_dir)
        deleta_dir_min(cliente, lista_qtd_dir, logger)

    else:
        logger.info(f"Quantidade de diretórios dentro do limite: {qtd_dir}")

def compacta_arquivos_carga(lista_clientes, logger):
    logger.debug(f"Iniciando compactação de arquivos para a lista de clientes: {lista_clientes}")
    
    for cliente in lista_clientes:
        logger.debug(f"Compactando arquivos para o cliente: {cliente}")
        
        data_ontem = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        data_hoje = datetime.now().strftime("%Y-%m-%d")
        
        dir_ontem = f"/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{data_ontem}"
        dir_hoje = f"/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/{data_hoje}"
        
        if os.path.exists(dir_ontem):
            logger.debug(f"Compactando arquivos no diretório de ontem: {dir_ontem}")
            os.system(f"find {dir_ontem} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")
            
            logger.debug(f"Compactando arquivos no diretório de hoje: {dir_hoje}")
            os.system(f"find {dir_hoje} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")
        else:
            logger.debug(f"Compactando arquivos no diretório de hoje: {dir_hoje}")
            os.system(f"find {dir_hoje} -type f ! -iname '*.gz' -exec gzip -f {{}} \\;")
            
    logger.info(f"Compactação de arquivos concluída para a lista de clientes: {lista_clientes}")

def deleta_dir_min(cliente, lista_qtd_dir, logger):
    logger.debug(f"Deletando o diretório mínimo para o cliente: {cliente}")
    
    if lista_qtd_dir:
        dir_min = min(lista_qtd_dir)
        logger.debug(f"Diretório mínimo encontrado: {dir_min}")
        
        os.system(f"rm -r /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/*{dir_min}")
        logger.info(f"Diretório mínimo deletado: /workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/tests/clientes/{cliente}/*{dir_min}")
    else:
        logger.warning(f"Lista vazia para o cliente {cliente}")
        print(f"Lista vazia para o cliente {cliente}")
