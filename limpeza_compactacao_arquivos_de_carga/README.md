# Limpeza e compactação de arquivos de carga

Este documento descreve o script main.py, que realiza o processo de limpeza e compactação de arquivos de carga para uma lista de clientes.

## main.py

O script main.py importa funções dos módulos utils, logger_config e client_operations e define a função principal main() para executar o processo completo de limpeza e compactação de arquivos de carga.

## Funções

main(): Função principal que executa o processo de limpeza e compactação de arquivos de carga. A função realiza as seguintes ações:

1. Configura o logger usando a função configure_logger() do módulo logger_config.
2. Inicia o processo de limpeza e compactação de arquivos de carga e registra no log.
3. Gera a lista de clientes usando a função gera_lista_clientes(logger) do módulo client_operations e registra a lista no log.
4. Compacta os arquivos de carga dos clientes usando a função compacta_arquivos_carga(lista_clientes, logger) do módulo client_operations.
5. Gera a lista de quantidade de diretórios para cada cliente usando a função gera_lista_qtd_dir(lista_clientes, logger) do módulo client_operations.
6. Registra a conclusão do processo de limpeza e compactação de arquivos de carga no log.
Execução

O script main.py é executado diretamente, ou seja, quando o nome do módulo é __main__. Ao executar o script, a função principal main() é chamada para realizar o processo completo de limpeza e compactação de arquivos de carga.

O main.py utiliza os módulos logger_config, utils e client_operations para gerenciar e executar as tarefas específicas de limpeza e compactação de arquivos de carga. Consulte o README.md relacionado a esses módulos para obter mais informações sobre suas funcionalidades e usos.