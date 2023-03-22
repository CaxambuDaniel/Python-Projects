import pickle
import os
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request

# Função para criar um serviço do Google API
def Create_Service(client_secret_file, api_name, api_version, *scopes):
    # Imprime informações sobre a API e escopos
    print(client_secret_file, api_name, api_version, scopes, sep='-')
    
    # Define variáveis com os parâmetros de entrada
    CLIENT_SECRET_FILE = client_secret_file
    API_SERVICE_NAME = api_name
    API_VERSION = api_version
    SCOPES = [scope for scope in scopes[0]]
    print(SCOPES)

    # Inicializa a variável 'cred' como None
    cred = None

    # Define o nome do arquivo pickle que armazena as credenciais da API
    pickle_file = f'token_{API_SERVICE_NAME}_{API_VERSION}.pickle'

    # Verifica se o arquivo pickle existe e carrega as credenciais
    if os.path.exists(pickle_file):
        with open(pickle_file, 'rb') as token:
            cred = pickle.load(token)

    # Verifica se as credenciais são inválidas ou inexistentes
    if not cred or not cred.valid:
        # Se as credenciais expiraram e possuem um refresh token, atualiza as credenciais
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        # Caso contrário, obtém as credenciais utilizando o arquivo client_secret_file e os escopos
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            cred = flow.run_local_server()

        # Salva as credenciais atualizadas no arquivo pickle
        with open(pickle_file, 'wb') as token:
            pickle.dump(cred, token)

    # Tenta criar e retornar o serviço da API
    try:
        service = build(API_SERVICE_NAME, API_VERSION, credentials=cred)
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    # Em caso de falha na conexão, imprime o erro e retorna None
    except Exception as e:
        print('Unable to connect.')
        print(e)
        return None

# Função para converter a data e hora em formato RFC 3339 (padrão usado em APIs do Google)
def convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt
