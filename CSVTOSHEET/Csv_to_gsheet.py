from Google import Create_Service
import pandas as pd
import numpy as np

CLIENT_SECRET_FILE = 'Credentials.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
gsheetId = '1oJCacGOW4PCQfCjLDb_EpwbQZdd7J_biIp7P048g28M'

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

def Export_Data_To_Sheets():
   URL = r'G:\Meu Drive\Data_Science\Dataset_baseMiddleware\base_middleware_tratado.csv'
   df = pd.read_csv(URL)
   df.replace(np.nan, '', inplace=True)

   response_date = service.spreadsheets().values().append(
       spreadsheetId=gsheetId,
       valueInputOption='RAW',
       range='base_middleware_tratada!A1',
       body=dict(
           majorDimension='ROWS',
           values=df.T.reset_index().T.values.tolist())
   ).execute()

Export_Data_To_Sheets()
