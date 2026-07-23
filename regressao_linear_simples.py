from algebra_linear import Vector
from estatistica import correlacao, desvio_padrao, media, media_deslocada
from typing import Tuple


def predict(alpha:float,beta:float, x_i:float) -> float:
    return beta * x_i +alpha

def error(alpha:float, beta: float, x_i:float, y_i:float) ->float:
    #calcula o erro de cada par
    return predict(alpha, beta,x_i) - y_i

def sum_of_sqerrors(alpha:float,beta:float,x:Vector,y:Vector)-> float:
    return sum(error(alpha,beta,x_i,y_i)**2 for x_i,y_i in zip(x,y))

def least_square_fit(x:Vector, y:Vector) -> Tuple[float,float]:

    """Encontra os quadrados mínimos de alpha e Beta. O cálculo está no caderno de Data Science"""
    beta = correlacao(x,y)*desvio_padrao(y)/desvio_padrao(x)
    alpha = media(y) - beta*media(x)
    return alpha , beta

def total_sum_of_squares(y:Vector)->float:
    #variação quadrática da média
    return sum(v**2 for v in media_deslocada(y))

def r_squared(alpha:float,beta:float,x:Vector,y:Vector)-> float:
    """A fração da variação em y capturada pelo modelo, igual a 1 - a fração da variação em y não
    capturada pelo modelo"""

    return 1.0 - (sum_of_sqerrors(alpha,beta,x,y)/total_sum_of_squares(y))