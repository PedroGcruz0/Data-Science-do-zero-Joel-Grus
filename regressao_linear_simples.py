


def predict(alpha:float,beta:float, x_i:float) -> float:
    return beta * x_i +alpha

def error(alpha:float, beta: float, x_i:float, y_i:float) ->float:
    #calcula o erro de cada par
    return predict(alpha, beta,x_i) - y_i

