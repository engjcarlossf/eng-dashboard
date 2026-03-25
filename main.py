from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# LIBERAÇÃO DE ACESSO (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite que seu site acesse a API
    allow_credentials=True,
    allow_methods=["*"], # Permite GET, POST, etc.
    allow_headers=["*"], # Permite todos os cabeçalhos
)

@app.get("/dados-producao")
def buscar_dados():
    # URL da Engemarko
    url = "http://179.124.195.91:1890/ADM_Engemarko/api/bi/producaoSigla?sigla=570"
    try:
        # Adicionamos um timeout para não travar o site se a API interna estiver lenta
        response = requests.get(url, timeout=15)
        return response.json()
    except Exception as e:
        return {"erro": str(e)}
