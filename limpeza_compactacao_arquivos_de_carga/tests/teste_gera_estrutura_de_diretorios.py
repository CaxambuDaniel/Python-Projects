import os
from datetime import date, timedelta

# Nome do diretório raiz
ROOT_DIR = ".."

# Lista de clientes
CLIENTS = ["cliente01", "cliente02", "cliente03", "cliente04", "cliente05"]

# Número de dias para gerar pastas com datas
NUM_DAYS = 3

# Data de hoje
today = date.today()

# Diretório de testes
tests_dir = os.path.abspath(os.path.dirname(__file__))

# Cria o diretório raiz se ainda não existir
root_dir = os.path.join(tests_dir, ROOT_DIR)
if not os.path.exists(root_dir):
    os.makedirs(root_dir)

# Percorre a lista de clientes
for client in CLIENTS:
    client_dir = os.path.join(root_dir, "tests", "cllientes", client)
    
    # Cria o diretório do cliente se ainda não existir
    if not os.path.exists(client_dir):
        os.makedirs(client_dir)
    
    # Percorre os últimos NUM_DAYS dias, incluindo a data de hoje
    for i in range(NUM_DAYS):
        current_date = today - timedelta(days=i)
        current_date_dir = current_date.strftime("%Y/%m/%d")
        current_date_full_dir = os.path.join(client_dir, current_date_dir)
        
        # Cria o diretório da data se ainda não existir
        if not os.path.exists(current_date_full_dir):
            os.makedirs(current_date_full_dir)
            
        # Cria 5 arquivos de carga na pasta
        for j in range(1, 6):
            file_name = f"arquivo_de_carga{j:02d}.txt"
            file_path = os.path.join(current_date_full_dir, file_name)
            
            with open(file_path, "w") as f:
                f.write(f"Conteúdo do arquivo {file_name}")
                
print("Estrutura de diretórios e arquivos criada com sucesso!")
