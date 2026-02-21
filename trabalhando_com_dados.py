from typing import List, Tuple 
import math
import random
from algebra_linear import (Vector,
                            produto_escalar,
                            calcula_media,
                            modulo,
                            multiplicar_escalar,
                            diferenca,
                            distancia)
from gradiente_descendente import passo_gradiente
from estatistica import variancia, desvio_padrao,media_deslocada

def centraliza_matriz(dados: List[Vector]) -> List[Vector]:
    """Ferramenta 2D: Centraliza uma matriz inteira (usada no PCA)"""
    media_vetorial = calcula_media(dados) # Usa a sua função de Álgebra
    return [diferenca(v, media_vetorial) for v in dados]

def escalona(data: List[Vector])-> Tuple[Vector, Vector]:
    dim = len(data[0])
    #calcula a média de cada dimensão
    media = calcula_media(data)
    #pega a lista [0.0] e repete dim vezes
    stdevs = [0.0]*dim
    for i in range(dim):
        #extrai a coluna i
        #o row[i] pega o elemento na posição e retorna como lista
        col_values = [row[i] for row in data]
        stdevs[i]=desvio_padrao(col_values)
    return media, stdevs

def rescalona(data: List[Vector]) -> List[Vector]:
    means, stdevs = escalona(data)
    
    rescaled_data = []
    for v in data:
        rescaled_vector = []
        for i in range(len(v)):
            if stdevs[i] > 0:
                rescaled_vector.append((v[i] - means[i]) / stdevs[i])
            else:
                rescaled_vector.append(v[i])
        rescaled_data.append(rescaled_vector)
    return rescaled_data

def direcao(w:Vector)->Vector:
    #calculo vetor unitário
    norma= modulo(w)
    return [w_i/norma for w_i in w]

def medir_variancia(data:List[Vector], w:Vector) -> float:
    """
    Mede o quanto os dados 'se espalham' na direção do vetor w.
    Queremos MAXIMIZAR isso no PCA.
    """
    w_dir = direcao(w)
    return sum(produto_escalar(v,w)**2 for v in data)
    #retorna a variação de x na direção de w

    #basicamente aqui se calcula em qual direção eu tenho o maior somatório do quadrado das somas

def directional_variance_gradient(data: List[Vector], w: Vector) -> Vector:
    """
    Retorna o gradiente da variancia direcional
    Nos diz para onde girar o vetor w para capturar mais variância.
    """
    w_dir = direcao(w)
    return [sum(2 * produto_escalar(v, w_dir) * v[i] for v in data) for i in range(len(w))]

def primeiro_componente_principal(data:List[Vector], n:int=100, tamanho_passo: float =0.1)->Vector:
    """
    Encontra a direção principal (o eixo onde os dados mais variam)
    usando Gradiente Descendente (mas subindo, pois queremos maximizar).
    """

    guess = [1.0 for _ in data[0]] # Chute inicial: vetor [1, 1, ...]
        
    for _ in range(n):
        dv = medir_variancia(data, guess)
        gradient = directional_variance_gradient(data, guess)
        
        # Somamos o gradiente (subimos o morro da variância)
        guess = passo_gradiente(guess, gradient, tamanho_passo)
        
    return direcao(guess)

def project(v: Vector, w: Vector) -> Vector:
    """Projeta o vetor v na direção w"""
    projection_length = produto_escalar(v, w)
    return multiplicar_escalar(projection_length, w)

# --- BLOCO DE TESTES ---
if __name__ == "__main__":
    
    print("--- Teste de Reescalonamento ---")
    # Dados: [Altura (cm), Peso (kg), Idade (anos)]
    # Note que Altura (170) é muito maior que Idade (30). Isso confunde o modelo.
    dados = [
        [170, 65, 30],
        [180, 80, 40],
        [160, 55, 20],
        [175, 70, 35]
    ]
    
    dados_padronizados = rescalona(dados)
    print("Dados Originais:", dados)
    print("Dados Reescalonados (Z-Score):")
    for linha in dados_padronizados:
        # Note que agora todos giram em torno de 0 (ex: -1.2, 0.5...)
        print([round(x, 2) for x in linha])

    print("\n--- Teste de PCA ---")
    # Dados simples 2D que esticam na diagonal
    dados_pca = [
        [10., 10.],
        [10.1, 10.2],
        [9.9, 9.8],
        [0., 0.] # Um outlier para puxar a média
    ]
    
    # Centralizar
    dados_centro = centraliza_matriz(dados_pca)
    
    # Achar o componente principal
    componente = primeiro_componente_principal(dados_centro)
    print(f"Direção Principal: {[round(x, 2) for x in componente]}")
    # Deve apontar na direção da diagonal (ex: [0.71, 0.71])