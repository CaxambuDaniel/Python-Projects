#!/bin/bash

# Verifica se o nome do projeto foi fornecido como parâmetro
if [ $# -eq 0 ]
then
  echo "Por favor, forneça um nome para o projeto."
  exit 1
fi

# Cria a estrutura de diretórios e arquivos para o projeto
mkdir -p $1/src/modules $1/tests
touch $1/src/main.py $1/src/modules/__init__.py $1/src/modules/module1.py $1/src/modules/module2.py $1/tests/test_module1.py $1/tests/test_module2.py $1/README.md $1/requirements.txt
