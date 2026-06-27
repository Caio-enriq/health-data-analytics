import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv('.env')

def buscar_idade(nome: str) -> int:
    """Busca a idade de uma pessoa."""
    return 30

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Qual a idade do Joao?',
    config=types.GenerateContentConfig(
        tools=[buscar_idade],
        temperature=0
    )
)
print("Function Call:", response.function_calls)
