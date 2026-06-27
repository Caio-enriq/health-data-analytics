import os, requests
from dotenv import load_dotenv

load_dotenv('.env')
app_id = os.environ.get("APPSHEET_APP_ID")
api_key = os.environ.get("APPSHEET_API_KEY")

url = f"https://api.appsheet.com/api/v2/apps/{app_id}/tables/4Documentos/Action"
headers = {"ApplicationAccessKey": api_key, "Content-Type": "application/json"}
body = {
    "Action": "Find",
    "Properties": {}
}

resp = requests.post(url, json=body, headers=headers)
if resp.status_code == 200:
    data = resp.json()
    if isinstance(data, list):
        print(f"Total records: {len(data)}")
    elif isinstance(data, dict) and "Rows" in data:
        print(f"Total records: {len(data['Rows'])}")
else:
    print(resp.text)
