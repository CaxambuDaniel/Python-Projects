import os

def gera_lista(comando, arquivo):
    # Executa o comando fornecido (geralmente um comando do sistema operacional) e salva a saída no arquivo especificado.
    os.system(comando)

    # Abre o arquivo especificado em modo de leitura.
    with open(arquivo) as f:
        # Lê todas as linhas do arquivo e remove os caracteres de nova linha e espaços em branco no início e no final de cada linha.
        # Adiciona cada linha limpa à lista.
        lista = [line.strip('\n').strip() for line in f.readlines()]

    # Retorna a lista de linhas limpas.
    return lista
