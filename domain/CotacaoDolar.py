from schemas.CotacaoOut import dolar
from services.CotacaoDolar import cotacao


def cotacao_dolar():

    valor_dolar = cotacao()
    alta = float(valor_dolar["USD"]["high"])
    baixa = float(valor_dolar["USD"]["low"])
    venda = float(valor_dolar["USD"]["bid"])
    return dolar(high=alta, low=baixa, bid=venda)
