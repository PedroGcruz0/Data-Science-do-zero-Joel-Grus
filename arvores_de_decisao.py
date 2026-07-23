from typing import List
import math

def entropy(class_probabilities:List[float])->float:
    """Caso haja uma lista de probabilidades de classe, calcule a entropia"""
    return sum(-p*math.log(p,2) for p in class_probabilities if p>0)


if __name__ == "__main__":
    assert entropy([1.0]) == 0
    assert entropy([0.5,0.5])
    