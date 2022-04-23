import requests
from fastapi import FastAPI

from domain.CotacaoDolar import cotacao_dolar
from schemas.CotacaoOut import dolar

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/cotacao")
async def say_hello():
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    return cotacao


@app.get("/cot", response_model=dolar)
async def say_hello():
    return cotacao_dolar()
