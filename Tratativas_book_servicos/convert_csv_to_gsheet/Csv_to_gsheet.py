from Google import Create_Service
import pandas as pd
import numpy as np

# Define as variáveis necessárias para criar o serviço da API do Google Sheets
CLIENT_SECRET_FILE = 'Credentials.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1oJCacGOW4PCQfCjLDb_EpwbQZdd7J_biIp7P048g28M'

# Cria o serviço da API do Google Sheets
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Função para exportar dados para o Google Sheets
def Export_Data_To_Sheets():
    # Define o caminho do arquivo CSV que será lido
    URL = r'G:\Meu Drive\Data_Science\Dataset_baseMiddleware\base_middleware_tratado.csv'
    
    # Lê o arquivo CSV e armazena em um DataFrame do Pandas
    df = pd.read_csv(URL)
    
    # Substitui valores NaN (Not a Number) por strings vazias
    df.replace(np.nan, '', inplace=True)

    # Envia os dados do DataFrame para o Google Sheets
    response_date = service.spreadsheets().values().append(
        spreadsheetId=gsheetId,
        valueInputOption='RAW',
        range='base_middleware_tratada!A1',
        body=dict(
            majorDimension='ROWS',
            # Transpõe o DataFrame e o converte em uma lista de valores
            values=df.T.reset_index().T.values.tolist())
    ).execute()

# Chama a função Export_Data_To_Sheets para enviar os dados para o Google Sheets
Export_Data_To_Sheets()
