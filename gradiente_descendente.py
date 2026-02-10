from typing import List, Callable, TypeVar,Iterator
import random
from algebra_linear import (Vector, 
                            produto_escalar,
                              modulo,
                              soma,
                              multiplicar_escalar,
                              distancia,
                              calcula_media,
                              soma_quadrados)

def derivada_parcial(f:Callable[[Vector], float],
                                v:Vector,
                                i:int,
                                h:float) -> float:
    #v é onde eu estou, i é o índice da direção que testaremos e h é o tamanho do passo
    
    #Calcula derivada parcial da i-ésima dimensão
    
    #lembrar que o enumerate retorna um dict com índice e valor!
    #repare que o j será o índice da lista e o v_j será o valor na posição j
    #vou fazer a verificação em qual componente do vetor eu quero adicionar o passo h(derivada parcial na componente)

    w= [v_j + (h if j == i else 0 ) for j,v_j in enumerate(Vector)]
    return (f(w)-f(v))/h
    #poderia ter usado Sympy e seria mais simples, mas é importante fazer assim.


def gradiente_estimado(f:Callable[[Vector],float],
                       v:Vector,
                       h: float =0.00001) -> Vector:
    
    #calcula o gradiente
    #é uma maneira bem elegante, i será cada componente
    return [derivada_parcial(f,v,i,h) for i in range (len(v))]

def passo_gradiente(v:Vector, gradiente:Vector,tamanho_passo:float)-> Vector:

    #da um passo de tamanho x na direção do gradiente
    #o tamanho do passo deve ser negativo pois queremos decrescimento
    assert len(v)==len(gradiente)
    passo= multiplicar_escalar(tamanho_passo,gradiente)
    return soma(v,passo)

def soma_de_quadrados_gradiente(v:Vector)->Vector:
    #derivada de x**2 é 2*x
    return [2*v_i for v_i in v]

T = TypeVar('T')

def minibatches(dataset:List[T],
                tamanho_batch: int,
                shuffle: bool=True)->Iterator[List[T]]:
    '''essa função é muito importante pois ela carrega uma quantidade de dados
    determinada. O tamanho do Batch diz essa quantidade
    porém eu tenho que pensar qual é o ideal, se for demais causará abismos'''

    '''importantíssimo usar o yield, pois ele funciona pausando a função para
    despausar da próxima vez que eu chamar, isso economiza muita memória'''

    #cria a lista de índices de acordo com o tamanho do batch dito
    inicio_batch = [inicio for inicio in range(0,len(dataset),tamanho_batch)]

    #embaralha se caso for solicitado
    if shuffle:
        random.shuffle(inicio_batch)

    
    for inicio in inicio_batch:
        fim_lista = inicio + tamanho_batch
        yield dataset[inicio:fim_lista]
        #basicamente é um loop que eu retorno uma lista com os pedaços do dataset

def minimize_epoch(target_fn: Callable[[Vector],float],
                   gradient_fn:Callable[[Vector],Vector],
                   theta_0:Vector,
                   tolerancia: float = 0.000001) -> Vector:
    """
    Tenta encontrar o vetor theta que minimiza a target_fn usando 
    Gradiente Descendente e regressão linear.
    (Repete até que a melhora seja menor que a tolerância).
    """
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta=theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)


    while True:
        gradient = gradient_fn(theta)
        
        #da passos de diferentes tamanhos em direção do gradiente
        next_thetas = [passo_gradiente(theta, gradient, -step) for step in step_sizes]
        
        #escolhe o passo que minimiza mais a função avaliando o gradiente calculado na anterior
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)
        
        # Se parou de melhorar (diferença menor que tolerância), paramos
        if abs(value - next_value) < tolerancia:
            return theta
        
        # Senão, atualizamos e continuamos
        theta, value = next_theta, next_value


def minimize_stochastic(target_fn: Callable[[Vector], float],
                        gradient_fn: Callable[[Vector], Vector],
                        x: List[Vector],
                        y: List[float],
                        theta_0: Vector,
                        alpha_0: float = 0.01) -> Vector:
    """
    Minimiza usando Gradiente Descendente Estocástico (SGD).
    Olha um exemplo por vez. É muito mais rápido para dados grandes.
    """
    data = list(zip(x, y))
    
    # theta é o nosso vetor de "pesos" que o modelo está aprendendo
    theta = theta_0
    
    # alpha é a velocidade de aprendizado (Learning Rate)
    alpha = alpha_0
    
    # min_theta e min_value guardam o melhor resultado que já vimos
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0
    
    # Se passar 100 épocas sem melhorar, a gente desiste (Early Stopping)
    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)

        if value < min_value:
            #achamos um novo mínimo!
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0 # Reseta a velocidade
        else:
            #não melhorou... vamos diminuir a velocidade e tentar de novo
            iterations_with_no_improvement += 1
            alpha *= 0.9

        #Passo Estocástico Atualiza para cada ponto de dado
        for x_i, y_i in data:
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = passo_gradiente(theta, gradient_i, -alpha)
            
        random.shuffle(data) # Embaralha para a próxima rodada
        
    return min_theta

# Função auxiliar de segurança (caso o cálculo dê erro matemático)
def safe(f: Callable[[Vector], float]) -> Callable[[Vector], float]:
    """Retorna uma nova função que é igual a f, mas retorna infinito se der erro"""
    def safe_f(x: Vector) -> float:
        try:
            return f(x)
        except:
            return float('inf') # Infinito = erro muito ruim
    return safe_f

# BLOCO DE TESTES
if __name__ == "__main__":
    
    print("Testando o Gradiente Descendente...")
    
    # 1. Escolhemos um ponto de partida aleatório (x=10, y=-10, z=5)
    v = [random.uniform(-10, 10) for i in range(3)]
    
    print(f"Começando em: {v}")
    
    # 2. Loop de Aprendizado (1000 épocas)
    for epoch in range(1000):
        # Calcula a direção da subida (gradiente)
        grad = soma_de_quadrados_gradiente(v)
        
        # Dá um passo para baixo (-0.01)
        v = passo_gradiente(v, grad, -0.01)
        
        if epoch % 100 == 0:
            print(f"Época {epoch}: {v}")
            
    print(f"Final (deveria ser perto de 0,0,0): {v}")
    print(f"Distância da origem: {distancia(v, [0,0,0])}")
