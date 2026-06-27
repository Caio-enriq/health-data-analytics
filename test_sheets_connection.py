import gspread
import json
import datetime
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

CREDENTIALS_FILE = 'credenciais.json'
SPREADSHEET_ID = '1xOentPWi5Yah9nPhtK4vi2-8KH7tSOT0TWuHl_XkIYk'

def main():
    print("Inicializando autenticação...")
    try:
        credentials = Credentials.from_service_account_file(
            CREDENTIALS_FILE, scopes=SCOPES)
        gc = gspread.authorize(credentials)
        print("✓ Autenticado com sucesso!")
        
        print(f"Tentando acessar planilha com ID: {SPREADSHEET_ID}")
        sh = gc.open_by_key(SPREADSHEET_ID)
        
        # Acessa a primeira aba
        worksheet = sh.get_worksheet(0)
        print(f"✓ Conectado à aba: {worksheet.title}")
        
        # Lê a primeira linha (cabeçalhos)
        headers = worksheet.row_values(1)
        print(f"Cabeçalhos encontrados: {headers}")
        
        # Cria uma linha de teste
        agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Vamos preencher a linha de teste com o tamanho exato de cabeçalhos, se existirem
        if not headers:
            test_row = ["DADO TESTE", agora]
        else:
            test_row = [f"Teste {agora}" if i==0 else "Val Teste" for i in range(len(headers))]
            
        print(f"Adicionando linha de teste: {test_row}")
        worksheet.append_row(test_row)
        print("✓ Linha de teste adicionada com sucesso!")
        
    except Exception as e:
        print(f"❌ Erro durante o processo: {e}")

if __name__ == '__main__':
    main()
