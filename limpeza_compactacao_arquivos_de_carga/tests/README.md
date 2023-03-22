# Script para criar estrutura de diretórios e arquivos de testes

Este script em Python cria uma estrutura de diretórios e arquivos de teste para o projeto "limpeza_compactacao_arquivos_de_carga". Essa estrutura inclui pastas para cada cliente e subpastas para cada uma das últimas três datas, incluindo a data de hoje. Dentro de cada pasta de data são criados cinco arquivos de carga.

## Como executar o script

1. Salve o script em um arquivo Python com o nome create_test_files.py.

2. Certifique-se de que o arquivo está salvo no diretório "tests" do projeto.

3. Abra um terminal na pasta "tests".

4. Execute o seguinte comando para executar o script:

python create_test_files.py

O script criará a estrutura de diretórios e arquivos descrita acima dentro do diretório "tests" do projeto.

## Variáveis de configuração

O script usa as seguintes variáveis de configuração para determinar o nome do diretório raiz, a lista de clientes, o número de dias para gerar pastas com datas e o diretório de testes:

1. ROOT_DIR = ".."

2. CLIENTS = ["cliente01", "cliente02", "cliente03", "cliente04", "cliente05"]

3. NUM_DAYS = 3

4. tests_dir = os.path.abspath(os.path.dirname(__file__))

Você pode modificar essas variáveis para personalizar a estrutura de diretórios e arquivos gerada pelo script. No entanto, certifique-se de que essas variáveis estão configuradas corretamente antes de executar o script.