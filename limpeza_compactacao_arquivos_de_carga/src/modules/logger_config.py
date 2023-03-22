import logging
from logging.handlers import TimedRotatingFileHandler
import arrow

# Cria uma subclasse personalizada de logging.Formatter para lidar com o fuso horário de Brasília.
class BrasiliaTimeFormatter(logging.Formatter):
    # Sobrescreve o método formatTime para converter o horário do registro para o fuso horário de Brasília.
    def formatTime(self, record, datefmt=None):
        # Converte o tempo do registro para um objeto arrow e ajusta para o fuso horário de Brasília.
        dt = arrow.get(record.created).to('America/Sao_Paulo')
        
        # Formata o tempo do registro de acordo com o formato especificado ou o formato padrão.
        if datefmt:
            formatted_time = dt.format(datefmt)
        else:
            formatted_time = dt.strftime(self.default_time_format)
        return formatted_time

def configure_logger():
    # Define o formato dos registros de log.
    log_format = "%(levelname)s %(asctime)s - %(message)s"
    
    # Cria um objeto formatter usando a classe BrasiliaTimeFormatter.
    formatter = BrasiliaTimeFormatter(log_format)
    
    # Define o caminho e o nome do arquivo de log.
    log_file = "/workspaces/Projetos_Python/limpeza_compactacao_arquivos_de_carga/log/limpeza_compactacao_carga.log"
    
    # Cria um manipulador de log que rotaciona o arquivo de log à meia-noite.
    handler = TimedRotatingFileHandler(log_file, when="midnight")
    
    # Define o formatter para o manipulador de log.
    handler.setFormatter(formatter)

    # Configura o logger e define o nível de log para DEBUG.
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    
    # Adiciona o manipulador de log ao logger.
    logger.addHandler(handler)
    
    # Retorna o logger configurado.
    return logger
