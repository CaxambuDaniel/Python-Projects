# Script de criação de projeto para GitHub Codespaces

Este script shell cria uma estrutura de diretórios e arquivos para um novo projeto no GitHub Codespaces.

## Pré-requisitos

Certifique-se de que o diretório /workspaces/Projetos_Python/ exista e que você tenha permissão para criar diretórios e arquivos nele. Caso o caminho do repositório seja diferente, atualize a variável REPO_ROOT no script para refletir o caminho correto.


## Como usar

1. Clone este repositório em seu GitHub Codespaces.

2. Abra o terminal do GitHub Codespaces e navegue até o diretório onde o repositório foi clonado.

3. Execute o seguinte comando, substituindo `nome_do_projeto` pelo nome desejado para o projeto:

	./create_project.sh nome_do_projeto

Este comando criará a estrutura de diretórios e arquivos correspondente ao nome do projeto fornecido.

4. Adicione o código do seu projeto aos arquivos correspondentes.

5. Se necessário, adicione as dependências do projeto ao arquivo `requirements.txt`.

6. Quando o projeto estiver pronto para ser compartilhado, faça o commit das alterações e faça o push para o repositório no GitHub.

## Estrutura de diretórios e arquivos

A estrutura de diretórios e arquivos criada pelo script é a seguinte:

- nome_do_projeto/

    - README.md
    - requirements.txt
    - src/
      - main.py
      - modules/
        - init.py
        - module1.py
        - module2.py
    - tests/
      - test_module1.py
      - test_module2.py

- `README.md`: um arquivo que descreve o projeto, sua finalidade e como usá-lo.

- `requirements.txt`: um arquivo que lista todas as dependências necessárias para o projeto ser executado, e que pode ser utilizado para instalar essas dependências automaticamente.

- `src/`: um diretório que contém o código-fonte do projeto.

  - `main.py`: um arquivo que contém o código principal do projeto.

  - `modules/`: um diretório que contém os módulos Python criados para o projeto.

    - `__init__.py`: um arquivo vazio que indica que o diretório é um pacote Python.

    - `module1.py`: um arquivo que contém um módulo Python.

    - `module2.py`: outro arquivo que contém um módulo Python.

- `tests/`: um diretório que contém os arquivos de teste para o projeto.

  - `test_module1.py`: um arquivo que contém testes para o módulo `module1.py`.

  - `test_module2.py`: outro arquivo que contém testes para o módulo `module2.py`.

Este script é uma forma simples e rápida de começar um novo projeto Python no GitHub Codespaces. Sinta-se à vontade para adaptar a estrutura de diretórios e arquivos criada pelo script às necessidades do seu projeto.