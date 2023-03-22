# MODULES

Este documento descreve os módulos utilizados no projeto de limpeza e compactação de arquivos de carga.
Esses módulos compõem a base do projeto de limpeza e compactação de arquivos de carga. Eles são utilizados pelo script principal main.py para executar o processo completo.

## logger_config.py
O módulo logger_config.py contém a configuração do logger utilizado no projeto. Ele fornece uma função para configurar o logger e uma classe personalizada para formatar o horário do registro de logs.

### Classes

BrasiliaTimeFormatter: Classe personalizada que herda de logging.Formatter e redefine o método formatTime para exibir o horário no fuso horário de Brasília.

### Funções

1. configure_logger(): Configura o logger com o formato de log, arquivo de log e rotação do arquivo de log. Retorna a instância do logger configurada.

## utils.py
O módulo utils.py fornece uma função utilitária para gerar uma lista a partir do conteúdo de um arquivo.

### Funções

1. gera_lista(comando, arquivo): Recebe um comando e um arquivo como argumentos, executa o comando, lê o arquivo e retorna uma lista com as linhas do arquivo.

## client_operations.py
O módulo client_operations.py contém as principais funções para gerenciar a limpeza e compactação de arquivos de carga para os clientes.

### Funções

1. gera_lista_clientes(logger): Gera a lista de clientes e registra a lista no log. Retorna a lista de clientes.

2. gera_lista_qtd_dir(lista_clientes, logger): Para cada cliente na lista de clientes, verifica a quantidade de diretórios e registra a quantidade no log.

3. checa_qtd_diretorios(cliente, logger): Verifica a quantidade de diretórios de um cliente específico. Se a quantidade de diretórios for maior que 2, gera uma lista com a quantidade de diretórios e deleta o diretório mínimo.

4. compacta_arquivos_carga(lista_clientes, logger): Compacta os arquivos de carga para os clientes na lista de clientes. Compacta os arquivos nos diretórios de ontem e hoje, se existirem.

5. deleta_dir_min(cliente, lista_qtd_dir, logger): Deleta o diretório mínimo de um cliente específico, se a lista de quantidade de diretórios não estiver vazia.

