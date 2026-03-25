from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# ESTE BLOCO É O QUE RESOLVE O "FAILED TO FETCH"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite que qualquer site (inclusive o seu) acesse a API
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados-producao")
def buscar_dados():
    # Sua URL da Engemarko
    url = "http://179.124.195.91:1890/ADM_Engemarko/api/bi/producaoSigla?sigla=570"
    try:
        response = requests.get(url, timeout=10)
        return response.json()
    except Exception as e:
        return {"erro": str(e)}
