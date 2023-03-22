# Limpeza e Compactação de Arquivos de Carga

Este projeto tem como objetivo realizar a limpeza e compactação de arquivos de carga para diversos clientes. O processo consiste em gerar uma lista de clientes, compactar os arquivos de carga e verificar a quantidade de diretórios de cada cliente.

## Estrutura do projeto

- limpeza_compactacao_arquivos_de_carga/

    - src/
        - main.py

        - modules/
        - logger_config.py
        - utils.py      
        - client_operations.py
        - README.md   
        - listas/
            - clientes.txt
            - qtd_dir.txt
            - README.md

    - tests/
        - gera_estrutura_de_diretorios.py
        - README.md
        - clientes/
            - cliente01/
            - cliente02/
            - cliente03/

    - logs/
        - limpeza_compactacao_carga.log

    - .gitignore

    - README.md

    - requirements.txt
	
## src/

Contém o arquivo principal main.py e a pasta modules/ com os módulos logger_config.py, utils.py e client_operations.py. Também possui a pasta listas/ para armazenar listas geradas durante a execução do script.

### main.py

Arquivo principal do projeto que chama as funções de compactação de arquivos e verificação de quantidade de diretórios.

### modules/

logger_config.py: Configura o logger para gerar logs durante a execução do script.

utils.py: Contém a função gera_lista() que gera listas a partir de comandos e arquivos.

client_operations.py: Contém as funções relacionadas às operações dos clientes, como compactar arquivos e gerar listas de quantidade de diretórios.

## tests/

Armazena o script gera_estrutura_de_diretorios.py e a pasta clientes/ com a estrutura de diretórios e arquivos de teste.

### gera_estrutura_de_diretorios.py

Script para gerar a estrutura de diretórios e arquivos de teste.

## logs/

Armazena os logs gerados durante a execução do script.

## .gitignore

Arquivo que define os arquivos e diretórios que não devem ser rastreados pelo Git.

## requirements.txt

Lista de dependências do projeto para serem instaladas com o pip.

# Instalação

## Clone o repositório:

1. git clone https://github.com/seu_usuario/limpeza_compactacao_arquivos_de_carga.git

2. Entre no diretório do projeto e crie um ambiente virtual Python:

    - cd limpeza_compactacao_arquivos_de_carga
    - python -m venv venv    

3. Ative o ambiente virtual:

    - No Windows: venv\Scripts\activate
    - No Linux/Mac: source venv/bin/activate

4. Instale as dependências:

    - pip install -r requirements.txt

# Execução

Para executar o script principal, execute o seguinte comando dentro do diretório `limpeza_compactacao