from typing import List
import math
from algebra_linear import soma_quadrados, produto_escalar


lista = List[float]

def media (x:lista) -> float:
    return sum(x)/len(x)

def media_deslocada(xs:lista) -> lista:
    #faço a diferença de cada elemento por sua média
    x_bar = media(xs)
    return [x-x_bar for x in xs]

def variancia (xs:lista) -> float:
    n = len(xs)
    assert n>=2 , "Requer pelo menos dois elementos"
    
    desvio = media_deslocada(xs)

    #calculo a soma dos quadrados do desvio e divide por n-1 (amostra)
    return(soma_quadrados(desvio)/(n-1))

def desvio_padrao (xs:lista) -> float:
    #o desvio padrão é a raiz da variância
    return math.sqrt(variancia(xs))


def covariancia (xs:lista, ys: lista ) -> float:
    assert len(xs) == len (ys) , "Tamanhos diferentes"
    return(produto_escalar(media_deslocada(xs), media_deslocada(ys))/(len(xs)-1))
    

def correlacao (xs:lista , ys:lista) -> float:
    desv_px = desvio_padrao(xs)
    desv_py = desvio_padrao(ys)
    if desv_px>0 and desv_py>0:
        return covariancia (xs,ys) /(desv_px*desv_py)
    else: return 0

