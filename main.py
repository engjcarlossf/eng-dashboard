from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# Isso é vital para o site funcionar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dados-producao")
def buscar_dados():
    # A URL da Engemarko que você passou
    url = "http://179.124.195.91:1890/ADM_Engemarko/api/bi/producaoSigla?sigla=570"
    response = requests.get(url)
    return response.json() # Devolve os dados crus para o site tratar
