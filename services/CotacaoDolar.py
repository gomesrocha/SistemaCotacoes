import requests


def cotacao():
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    valores = requisicao.json()
    return valores
