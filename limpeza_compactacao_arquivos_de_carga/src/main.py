# main.py
from modules.utils import gera_lista
from modules.logger_config import configure_logger
from modules.client_operations import (gera_lista_clientes, gera_lista_qtd_dir, compacta_arquivos_carga)

# Função principal que executa o processo de limpeza e compactação de arquivos de carga
def main():
    # Configura o logger
    logger = configure_logger()
    logger.debug("Iniciando o processo de limpeza e compactação de arquivos de carga")

    # Gera a lista de clientes
    lista_clientes = gera_lista_clientes(logger)
    logger.debug(f"Lista de clientes gerada: {lista_clientes}")

    # Compacta os arquivos de carga dos clientes
    compacta_arquivos_carga(lista_clientes, logger)

    # Gera a lista de quantidade de diretórios para cada cliente
    gera_lista_qtd_dir(lista_clientes, logger)

    # Registra o fim do processo de limpeza e compactação de arquivos de carga
    logger.debug("Processo de limpeza e compactação de arquivos de carga concluído")

# Executa a função principal quando o script é executado diretamente
if __name__ == "__main__":
    main()
