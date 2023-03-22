# logger_config.py
import logging

def configure_logger():
    logging.basicConfig(filename="/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/log/limpeza_compactacao_carga.log",
                        format="%(levelname)s %(asctime)s - %(message)s",
                        filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    return logger
