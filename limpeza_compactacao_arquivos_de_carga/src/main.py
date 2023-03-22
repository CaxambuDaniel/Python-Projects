# main.py
from modules.utils import gera_lista
from modules.logger_config import configure_logger
from modules.client_operations import (gera_lista_clientes, gera_lista_qtd_dir, compacta_arquivos_carga)

def main():
    logger = configure_logger()
    logger.debug("Iniciando o processo de limpeza e compactação de arquivos de carga")
    
    lista_clientes = gera_lista_clientes(logger)
    logger.debug(f"Lista de clientes gerada: {lista_clientes}")
    
    compacta_arquivos_carga(lista_clientes, logger)
    
    gera_lista_qtd_dir(lista_clientes, logger)
    logger.debug("Processo de limpeza e compactação de arquivos de carga concluído")

if __name__ == "__main__":
    main()
