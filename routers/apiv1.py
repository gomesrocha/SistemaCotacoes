from fastapi import APIRouter
from domain.CotacaoDolar import cotacao_dolar
from schemas.CotacaoOut import dolar
import requests
router = APIRouter()




@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@router.get("/cotacao")
async def cotacao():
    requisicao = requests.get("https://economia.awesomeapi.com.br/all/USD-BRL")
    cotacao = requisicao.json()
    return cotacao

@router.get("/cot", response_model=dolar)
async def cot():
    return cotacao_dolar()
