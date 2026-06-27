from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import gspread
from google.oauth2.service_account import Credentials
import os, re, json
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

app = FastAPI(title="HealthData Dashboard API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
def serve_dashboard():
    p = os.path.join(os.path.dirname(os.path.dirname(__file__)), "dashboard.html")
    return FileResponse(p) if os.path.exists(p) else {"error": "dashboard.html not found"}

@app.get("/ai_avatar.png")
def serve_avatar():
    p = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ai_avatar.png")
    return FileResponse(p) if os.path.exists(p) else {"error": "ai_avatar.png not found"}

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
SPREADSHEET_ID = '1xOentPWi5Yah9nPhtK4vi2-8KH7tSOT0TWuHl_XkIYk'

def get_sheet():
    base = os.path.dirname(os.path.dirname(__file__))
    cred_path = os.path.join(base, 'credenciais.json')
    if not os.path.exists(cred_path):
        cred_path = 'credenciais.json'
    if not os.path.exists(cred_path):
        raise Exception("Arquivo credenciais.json não encontrado")
    creds = Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    gc = gspread.authorize(creds)
    return gc.open_by_key(SPREADSHEET_ID)

def humanize_fn(fn: str) -> str:
    """Converte nomes de função camelCase para português legível."""
    mapping = {
        'registrarCaixasNoDocZ': 'Registrar Caixas no DocZ',
        'registrarDocumentosNoDocZ': 'Registrar Documentos no DocZ',
        'processarIACaixas': 'Processar IA — Caixas',
        'processarIADocumentos': 'Processar IA — Documentos',
    }
    if fn in mapping:
        return mapping[fn]
    # Fallback: split camelCase
    s = re.sub(r'([A-Z])', r' \1', fn).strip()
    return s.title()

def read_ws(ws):
    """Lê todos os valores de uma aba e retorna lista de dicts com keys normalizadas."""
    vals = ws.get_all_values()
    if not vals or len(vals) < 2:
        return []
    headers = [str(h).strip() for h in vals[0]]
    records = []
    for row in vals[1:]:
        rec = {}
        for i, h in enumerate(headers):
            rec[h] = row[i] if i < len(row) else ''
        records.append(rec)
    return records

@app.get("/api/data")
def get_all_data():
    try:
        sh = get_sheet()
        ws_map = {ws.title: ws for ws in sh.worksheets()}

        def load(name):
            for k, ws in ws_map.items():
                if name.lower() in k.lower():
                    return read_ws(ws)
            return []

        execs_raw = load('Execucoes')
        errs_raw  = load('Erros')
        itens_raw = load('Itens_Processados')
        logs_raw  = load('Logs')
        cfg_raw   = load('Config')
        smoke_raw = load('Smoke')
        dash_raw  = load('Dashboard')

        # Normalizar Execucoes — primeiro col é 'se ' (uuid), mapear para execucao_id
        execs = []
        for r in execs_raw:
            uid = r.get('se ', r.get('se', ''))
            execs.append({
                'execucao_id':     uid,
                'iniciado_em':     r.get('iniciado_em', ''),
                'finalizado_em':   r.get('finalizado_em', ''),
                'duracao_ms':      r.get('duracao_ms', ''),
                'funcao':          r.get('funcao', ''),
                'funcao_label':    humanize_fn(r.get('funcao', '')),
                'status':          r.get('status', r.get('status ', '')).strip(),
                'modo':            r.get('modo', ''),
                'tamanho_lote':    r.get('tamanho_lote', ''),
                'total_encontrado':r.get('total_encontrado', ''),
                'total_processado':r.get('total_processado', ''),
                'total_sucesso':   r.get('total_sucesso', ''),
                'total_erro':      r.get('total_erro', ''),
                'mensagem_resumo': r.get('mensagem_resumo', ''),
                'primeiro_id_appsheet': r.get('primeiro_id_appsheet', ''),
                'primeira_etiqueta':    r.get('primeira_etiqueta', ''),
                'ultimo_id_appsheet':   r.get('ultimo_id_appsheet', ''),
                'ultima_etiqueta':      r.get('ultima_etiqueta', ''),
                'itens_resumo':         r.get('itens_resumo', ''),
            })

        # Normalizar Erros — primeiro col é 'eu mostr' (uuid do erro)
        errs = []
        for r in errs_raw:
            uid = r.get('eu mostr', r.get('eu_mostr', ''))
            errs.append({
                'erro_id':      uid,
                'criado_em':    r.get('criado_em', ''),
                'status_erro':  r.get('status_erro', ''),
                'execucao_id':  r.get('execucao_id', ''),
                'funcao':       r.get('funcao', ''),
                'funcao_label': humanize_fn(r.get('funcao', '')),
                'tipo_entidade':r.get('tipo_entidade', ''),
                'id_appsheet':  r.get('id_appsheet', ''),
                'etiqueta':     r.get('etiqueta', ''),
                'codigo_erro':  r.get('codigo_erro', ''),
                'mensagem_erro':r.get('mensagem_erro', ''),
                'tentativas':   r.get('tentativas', ''),
                'resolvido_em': r.get('resolvido_em', ''),
                'observacao':   r.get('observacao', ''),
            })

        # Smoke Tests
        smoke = []
        for r in smoke_raw:
            smoke.append({
                'teste_id':     r.get('teste_id', ''),
                'criado_em':    r.get('criado_em', ''),
                'tipo_entidade':r.get('tipo_entidade', ''),
                'id_appsheet':  r.get('id_appsheet', ''),
                'etiqueta':     r.get('etiqueta', ''),
                'funcao_alvo':  r.get('funcao_alvo', ''),
                'funcao_label': humanize_fn(r.get('funcao_alvo', '')),
                'status_teste': r.get('status_teste', ''),
                'resultado':    r.get('resultado', ''),
                'observacao':   r.get('observacao', ''),
            })

        # Calcular KPIs dinamicamente a partir dos itens
        total_cb = sum(1 for i in itens_raw if i.get('tipo_entidade', '') == 'CAIXA')
        total_dc = sum(1 for i in itens_raw if i.get('tipo_entidade', '') == 'DOCUMENTO')
        ok_cb = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'CAIXA' and i.get('status_item', '') == 'SUCESSO')
        ok_dc = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'DOCUMENTO' and i.get('status_item', '') == 'SUCESSO')
        erros_abertos = sum(1 for e in errs if e['status_erro'] == 'ABERTO')
        tsc = round(ok_cb / total_cb * 100, 1) if total_cb else 0
        tsd = round(ok_dc / total_dc * 100, 1) if total_dc else 0

        kpis = {
            'TOTAL_CAIXAS_REGISTRADAS': str(total_cb),
            'TOTAL_DOCUMENTOS_REGISTRADOS': str(total_dc),
            'TOTAL_EXECUCOES': str(len(execs)),
            'TOTAL_ERROS_ABERTOS': str(erros_abertos),
            'TAXA_SUCESSO_CAIXAS': str(tsc),
            'TAXA_SUCESSO_DOCUMENTOS': str(tsd),
        }

        return {
            'execs': execs,
            'errs':  errs,
            'itens': itens_raw,
            'logs':  logs_raw,
            'cfg':   cfg_raw,
            'smoke': smoke,
            'dash':  dash_raw,
            'kpis':  kpis,
        }
    except Exception as e:
        print(f"Erro get_all_data: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/documento/{etiqueta}")
def get_document_details(etiqueta: str):
    try:
        sh = get_sheet()
        ws_itens = sh.worksheet("Itens_Processados")
        records = read_ws(ws_itens)

        doc = next((r for r in records
                    if r.get('etiqueta', '').upper() == etiqueta.upper()), None)

        if not doc:
            raise HTTPException(status_code=404, detail="Documento não encontrado na planilha")

        app_id  = os.environ.get("APPSHEET_APP_ID")
        api_key = os.environ.get("APPSHEET_API_KEY")
        appsheet_data = None

        if app_id and api_key:
            url = f"https://api.appsheet.com/api/v2/apps/{app_id}/tables/4Documentos/Action"
            headers = {"ApplicationAccessKey": api_key, "Content-Type": "application/json"}
            body = {
                "Action": "Find",
                "Properties": {
                    "Selector": f"Filter(4Documentos, [EtiquetaDocumento] = '{etiqueta}')"
                }
            }
            try:
                resp = requests.post(url, json=body, headers=headers, timeout=10)
                if resp.status_code == 200:
                    result = resp.json()
                    if isinstance(result, list) and result:
                        appsheet_data = result[0]
                    elif isinstance(result, dict) and result.get("Rows"):
                        appsheet_data = result["Rows"][0]
            except Exception as ae:
                print(f"AppSheet error: {ae}")

        if not appsheet_data:
            appsheet_data = {"status_sync": "FALHA", "nota": "Nenhum registro encontrado no AppSheet para esta etiqueta."}
        else:
            appsheet_data["status_sync"] = "SINCRONIZADO"

        return {"dados_planilha": doc, "dados_appsheet": appsheet_data}

    except HTTPException:
        raise
    except Exception as e:
        print(f"Erro get_document_details: {e}")
        raise HTTPException(status_code=500, detail=str(e))

def buscar_documento_appsheet(coluna: str, valor: str) -> str:
    """Busca registros na base de dados AppSheet (tabela 4Documentos). Use para buscar dados de pacientes, prontuários, status OCR, ou caixas.
    Args:
        coluna: Nome da coluna (ex: 'EtiquetaDocumento', 'NomePaciente', 'CaixaID', 'NumeroProntuario').
        valor: Valor para buscar.
    """
    app_id = os.environ.get("APPSHEET_APP_ID")
    api_key = os.environ.get("APPSHEET_API_KEY")
    if not app_id or not api_key:
        return "Erro: Credenciais do AppSheet não configuradas."
    url = f"https://api.appsheet.com/api/v2/apps/{app_id}/tables/4Documentos/Action"
    headers = {"ApplicationAccessKey": api_key, "Content-Type": "application/json"}
    body = {
        "Action": "Find",
        "Properties": {
            "Selector": f"Filter(4Documentos, [{coluna}] = '{valor}')"
        }
    }
    try:
        resp = requests.post(url, json=body, headers=headers, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            rows = data if isinstance(data, list) else data.get("Rows", [])
            if not rows:
                return "Nenhum registro encontrado."
            # Retorna até 5 resultados para não estourar o limite de tokens
            return json.dumps(rows[:5], ensure_ascii=False)
        return f"Erro na busca: HTTP {resp.status_code}"
    except Exception as e:
        return f"Erro na requisição: {str(e)}"

class ChatRequest(BaseModel):
    pergunta: str

@app.post("/api/chat")
def ai_chat(req: ChatRequest):
    try:
        sh = get_sheet()
        execs_raw = read_ws(sh.worksheet("Execucoes"))
        errs_raw  = read_ws(sh.worksheet("Erros"))
        itens_raw = read_ws(sh.worksheet("Itens_Processados"))

        total_cb = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'CAIXA')
        total_dc = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'DOCUMENTO')
        ok_cb = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'CAIXA' and i.get('status_item') == 'SUCESSO')
        ok_dc = sum(1 for i in itens_raw if i.get('tipo_entidade') == 'DOCUMENTO' and i.get('status_item') == 'SUCESSO')
        erros_abertos = [e for e in errs_raw if e.get('status_erro') == 'ABERTO']
        tsc = round(ok_cb / total_cb * 100, 1) if total_cb else 0
        tsd = round(ok_dc / total_dc * 100, 1) if total_dc else 0

        err_por_codigo = {}
        for e in erros_abertos:
            c = e.get('codigo_erro', 'DESCONHECIDO')
            err_por_codigo[c] = err_por_codigo.get(c, 0) + 1
        err_por_etiqueta = [(e.get('etiqueta',''), e.get('codigo_erro',''), e.get('mensagem_erro','')[:80]) for e in erros_abertos[:20]]

        exec_resumo = []
        for e in execs_raw[-30:]:
            uid = e.get('se ', e.get('se', ''))[:8]
            exec_resumo.append(
                f"ID:{uid} | Status:{e.get('status','')} | Fn:{humanize_fn(e.get('funcao',''))} | "
                f"Sucesso:{e.get('total_sucesso','')} | Erro:{e.get('total_erro','')} | Msg:{e.get('mensagem_resumo','')[:60]}"
            )

        contexto = f"""Você é o Assistente de Observabilidade da Plataforma HealthData — sosdocs.
Sua missão: responder perguntas de forma DIRETA, FIRME e PROFISSIONAL, como um analista de dados sênior.
Você tem acesso à função `buscar_documento_appsheet` para buscar dados na database AppSheet se o usuário perguntar sobre pacientes, prontuários, status OCR ou detalhes que não estão no resumo.

=== RESUMO DA PLANILHA ===
📦 TOTAIS:
- Caixas (CB): {total_cb} (Sucesso: {tsc}%)
- Documentos (DC): {total_dc} (Sucesso: {tsd}%)
- Erros Abertos: {len(erros_abertos)}

🚨 ERROS: {json.dumps(err_por_codigo, ensure_ascii=False)}
{chr(10).join([f'  • {et} | {cd} | {mg}' for et,cd,mg in err_por_etiqueta])}

⚙️ EXECUÇÕES:
{chr(10).join(exec_resumo)}
"""

        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            return {"resposta": "⚠️ Chave Gemini não configurada no `.env` do backend."}

        client = genai.Client(api_key=api_key)
        
        from google.genai import types
        chat = client.chats.create(
            model='gemini-2.5-flash',
            config=types.GenerateContentConfig(
                tools=[buscar_documento_appsheet],
                system_instruction=contexto,
                temperature=0.3
            )
        )
        response = chat.send_message(req.pergunta)
        return {"resposta": response.text}

    except Exception as e:
        return {"resposta": f"⚠️ Erro ao processar: {str(e)}"}
