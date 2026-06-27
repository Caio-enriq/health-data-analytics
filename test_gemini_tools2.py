import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv('.env')

def buscar_idade(nome: str) -> int:
    """Busca a idade de uma pessoa.
    Args:
        nome: nome da pessoa.
    """
    print("CHAMOU A FUNCAO", nome)
    return 30

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=types.GenerateContentConfig(
        tools=[buscar_idade],
        temperature=0
    )
)
resp = chat.send_message("Qual a idade do Joao?")
print(resp.text)
