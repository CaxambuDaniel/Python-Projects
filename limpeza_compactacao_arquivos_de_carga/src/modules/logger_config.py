import logging
from logging.handlers import TimedRotatingFileHandler
import arrow

class BrasiliaTimeFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = arrow.get(record.created).to('America/Sao_Paulo')
        
        if datefmt:
            formatted_time = dt.format(datefmt)
        else:
            formatted_time = dt.strftime(self.default_time_format)
        return formatted_time

def configure_logger():
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    formatter = BrasiliaTimeFormatter(log_format)
    
    log_file = "/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/src/log/limpeza_compactacao_carga.log"
    handler = TimedRotatingFileHandler(log_file, when="midnight")
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger
