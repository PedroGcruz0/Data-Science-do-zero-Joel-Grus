# probability.py
import math

def normal_cdf(x: float, mu: float = 0, sigma: float = 1) -> float:
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p: float, mu: float = 0, sigma: float = 1, tolerance: float = 0.00001) -> float:
    """Encontra o Z tal que a probabilidade de ser menor que Z é p (Binary Search)"""
    
    # Se não for padrão, ajustamos a escala depois
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    
    low_z = -10.0                      # Z muito baixo (perto de 0%)
    hi_z  =  10.0                      # Z muito alto (perto de 100%)
    mid_z = 0.0
    
    # Fica procurando até chegar muito perto da probabilidade 'p'
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2     # Tenta o meio
        mid_p = normal_cdf(mid_z)      # Vê quanto dá a prob no meio
        
        if mid_p < p:
            low_z = mid_z              # O valor está acima do meio
        else:
            hi_z = mid_z               # O valor está abaixo do meio
            
    return mid_z