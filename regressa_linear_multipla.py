from algebra_linear import produto_escalar, Vector
from regressao_linear_simples import total_sum_of_squares
from typing import List

def predict(x:Vector,beta:Vector) -> float:
    """Pressupõe que o primeiro elemento é 1"""
    return produto_escalar(x,beta)

def error(x:Vector,y:float,beta:Vector) -> float:
    return predict(x,beta) - y

def squared_error(x:Vector,y:float,beta:Vector) -> float:
    return error(x,y,beta)**2

def sqerror_gradient(x:Vector,y:float,beta:Vector) ->Vector:
    err = error(x,y,beta)
    return [2*err*x_i for x_i in x]
def multiple_r_squared(xs:List[Vector],ys:Vector,beta:Vector) -> float:
    sum_of_squared_errors = sum(error(x,y,beta)**2 for x,y in zip(xs,ys))
    1.0- sum_of_squared_errors/total_sum_of_squares


if __name__ == '__main__':
    x=[1,2,3]
    y=30
    beta=[4,4,4] #logo a previsão é de 4 + 8 + 12 = 24
    assert error(x,y,beta) == -6
    assert squared_error(x,y,beta)== 36
    assert sqerror_gradient(x,y,beta)==[-12,-24,-36]