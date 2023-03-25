#!/bin/bash

# Verifica se o nome do projeto foi fornecido como parâmetro
if [ $# -eq 0 ]
then
  echo "Por favor, forneça um nome para o projeto."
  exit 1
fi

# Caminho para a raiz do repositório
REPO_ROOT="/workspaces/Projetos_Python/"

# Cria a estrutura de diretórios e arquivos para o projeto
mkdir -p "$REPO_ROOT/$1/src/modules" "$REPO_ROOT/$1/tests"
touch "$REPO_ROOT/$1/src/main.py" "$REPO_ROOT/$1/src/modules/__init__.py" "$REPO_ROOT/$1/src/modules/module1.py" "$REPO_ROOT/$1/src/modules/module2.py" "$REPO_ROOT/$1/tests/test_module1.py" "$REPO_ROOT/$1/tests/test_module2.py" "$REPO_ROOT/$1/README.md" "$REPO_ROOT/$1/requirements.txt"
