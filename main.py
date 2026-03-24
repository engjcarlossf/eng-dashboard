from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import pandas as pd

app = FastAPI()

# Permite que o seu site engjcarlos.com acesse os dados sem bloqueios
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"status": "Online", "msg": "API de Engenharia Eng. Jean Carlos"}

@app.get("/producao")
def obter_producao(sigla: str = "570"):
    # URL da API da Engemarko que você forneceu
    url = f"http://179.124.195.91:1890/ADM_Engemarko/api/bi/producaoSigla?sigla={sigla}"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            dados = response.json()
            
            # Usando Pandas para processar (muito mais rápido que Excel)
            df = pd.DataFrame(dados)
            
            # Exemplo de processamento: volume total
            # Nota: Ajuste o nome da coluna 'volume' conforme o retorno real da sua API
            vol_total = 0
            if not df.empty and 'volume' in df.columns:
                vol_total = float(df['volume'].sum())

            return {
                "sigla": sigla,
                "total_registros": len(df),
                "volume_total_m3": vol_total,
                "dados": dados
            }
        return {"erro": "Não foi possível acessar a API da Engemarko"}
    except Exception as e:
        return {"erro": str(e)}

@app.get("/global")
def informacao_global():
    url = "http://179.124.195.91:1890/ADM_Engemarko/api/bi/informacaoGlobalPeca"
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        return {"erro": str(e)}
