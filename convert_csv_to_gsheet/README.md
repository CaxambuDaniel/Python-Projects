# Google Sheets API - CSV to Google Sheets

Este projeto demonstra como utilizar a Google Sheets API para ler dados de um arquivo CSV e exportá-los para uma planilha do Google Sheets.

## Arquivos

### 1. google.py

O arquivo `google.py` contém funções para criar um serviço do Google API e converter datas para o formato RFC 3339. As funções incluem:

- `Create_Service(client_secret_file, api_name, api_version, *scopes)`: Cria e retorna um serviço do Google API a partir do arquivo de segredo do cliente e dos escopos necessários.
- `convert_to_RFC_datetime(year=1900, month=1, day=1, hour=0, minute=0)`: Converte a data e a hora fornecidas para o formato RFC 3339, que é o padrão usado pelas APIs do Google.

### 2. csv_to_gsheet.py

O arquivo `csv_to_gsheet.py` utiliza a função `Create_Service` do módulo `Google` para criar um serviço da API do Google Sheets. Ele contém a função `Export_Data_To_Sheets()`, que lê um arquivo CSV, substitui os valores NaN por strings vazias e envia os dados para uma planilha do Google Sheets.

## Como usar

1. Certifique-se de ter instalado as bibliotecas necessárias:

pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client pandas

2. Baixe e salve o arquivo de credenciais da API do Google como `Credentials.json`. Para saber como criar um arquivo de credenciais, consulte a [documentação oficial do Google](https://developers.google.com/workspace/guides/create-credentials).

3. Atualize o caminho do arquivo CSV e o ID da planilha do Google Sheets no arquivo `csv_to_gsheet.py`.

4. Execute o arquivo `csv_to_gsheet.py`:

python csv_to_gsheet.py

Os dados do arquivo CSV serão enviados para a planilha do Google Sheets especificada.
