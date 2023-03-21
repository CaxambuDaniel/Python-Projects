import os
from datetime import datetime, timedelta

# Define os clientes do projeto
clientes = ["cliente01", "cliente02", "cliente03", "cliente04", "cliente05"]

# Define as datas para criação dos arquivos de carga
hoje = datetime.now()
ontem = hoje - timedelta(days=1)
anteontem = hoje - timedelta(days=2)
datas = [hoje, ontem, anteontem]

# Define o diretório raiz do projeto
projeto = "limpeza_compactacao_arquivos_de_carga"
tests_dir = os.path.join(projeto, "tests")

# Cria a estrutura de diretórios e arquivos para cada cliente e cada data
for cliente in clientes:
    cliente_dir = os.path.join(tests_dir, "clientes", cliente)
    for data in datas:
        data_dir = os.path.join(cliente_dir, data.strftime("%Y/%m/%d"))
        os.makedirs(data_dir, exist_ok=True)
        for i in range(1, 6):
            arquivo = f"arquivo_de_carga{i:02d}.txt"
            open(os.path.join(data_dir, arquivo), "a").close()
