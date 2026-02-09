from typing import List
import math

Vector= List[float]


#lembrar de adicionar o if __name__ == "__main__": se quiser adicionar códigos além de funções
def verificar_componentes(v: Vector, w: Vector) -> bool:
    assert len(v)==len(w)
    return True


#outra maneira de fazer a soma
def soma(v: Vector, w: Vector) -> Vector:
    """Soma elementos correspondentes de dois vetores"""
    assert len(v) == len(w), "vetores devem ter o mesmo tamanho"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def diferenca(v:Vector , w: Vector):
   assert len(v)==len(w)

   #importante aprender essa maneira de fazer, pois toma muito tempo e é mais pythonic
    # O v_i vai assumar um índice do primeiro elemento e o w_i vai assumir o outro
   a =[ v_i - w_i for v_i,w_i in zip(v,w)]
   return a

        
def soma_varios(vectors: Vector) -> Vector:
    #essa função vai retornar a soma das componentes para uma lista de vetores
    assert vectors, 'Insira algo'
    #prestar atenção no comando all, pois ele vai verificar toda a lista 
    #e retornar um booleano, vai receber uma lista
    numero_elementos = len(vectors[0])
    assert(all(len(v_i)==numero_elementos for v_i in vectors)) , "Todos os elementos não tem o mesmo tamanho"

    return [sum(vector[i] for vector in vectors) for i in range(numero_elementos)]

#faça isso para cada i in range (número elementos), confesso que é um pouco confuso
#lembrando que os vetores tem duas componentes


def multiplicar_escalar(c:float, vetor: Vector) -> Vector:
    #basicamente peguei um vetor com i dimenções e multipliquei por um float
    return [c*i for i in vetor]


def calcula_media (v:Vector) -> Vector:
    #pego uma lista de vetores, calculo a média de cada um,
    tamanho = len(v)
    return [multiplicar_escalar(1/tamanho , soma_varios(v))]

def produto_escalar(v:Vector,w: Vector) -> float:
    #mesma ideia das somas
    assert verificar_componentes(v,w) == True
    return sum(v_i*w_i for v_i,w_i in zip(v,w))


def soma_quadrados (v:Vector) -> float:
    return(produto_escalar(v,v))


def modulo (v:Vector) -> float:
    #calculo a raíz da soma dos quadrados
    return math.sqrt(soma_quadrados(v))

def distancia (v:Vector , w:Vector) -> float:

    return modulo(diferenca(v,w))

if __name__ == "__main__":
    """Digite atributos e comandos aqui"""