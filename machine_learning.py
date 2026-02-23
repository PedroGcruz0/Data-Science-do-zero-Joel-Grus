import random
from typing import TypeVar, List, Tuple

X = TypeVar('X')
Y = TypeVar('Y')

def split_data(data:List[X],prob:float)-> Tuple[List[X],List[X]]:
    """Divida os dados em frações [prob,1-prob]"""
    data = data[:] #faço uma cópia dos dados
    random.shuffle(data) #bagunça a ordem dos itens
    cut = int(len(data)*prob) #quantos% da imagem eu quero treinar minha IA 
    return data[:cut],data[cut:] #divido a lista aleatória nesses dois pontos

#se forem pares?
def train_test_split(xs:List[X],
                     ys:List[Y],
                     teste_pct:float) -> Tuple[List[X],List[X],List[Y],List[Y]]:
    #gerar de dividir os índices
    idxs = [i for i in range (len(xs))]
    train_idxs, test_idxs = split_data(idxs,1 - teste_pct)
    return ([xs[i] for i in train_idxs],
            [xs[i] for i in test_idxs],
            [ys[i] for i in train_idxs],
            [ys[i] for i in test_idxs])

#computar estatísticas
def accuracy(tp:int,fp:int,fn:int,tn:int) -> float:
    correct = tp+tn
    total = tp+fp+fn+tn
    return correct/total

def precision(tp:int,fp:int,fn:int,tn:int)->float:
    return tp/(tp+fp)

def recall(tp:int,fp:int,fn:int,tn:int)->float:
    return tp/(tp+fn)

def f1_score(tp:int,fp:int,fn:int,tn:int)->float:
    p = precision(tp,fp,fn,tn)
    r = recall(tp,fp,fn,tn)
    return 2*p*r/(p+r)


# Bloco de Testes
if __name__ == '__main__':
    #testando split data
    data = [n for n in range(1000)]
    train, test = split_data(data,0.75)
    assert len(train) == 750
    assert len (test) == 250
    assert sorted(test + train) == data

    #testando train test split
    xs = [x for x in range(1000)]
    ys = [2*x for x in xs]
    x_train,x_test,y_train,y_test = train_test_split(xs,ys,0.33)
    assert all(y==2*x for x, y in zip (x_train,y_train))
    assert all(y==2*x for x, y in zip (x_test,y_test))
    
    #testando o accuracy
    assert accuracy(70,4930,13930,981070) == 0.98114
    assert precision(70,4930,13930,981070) == 0.014
    assert recall(70,4930,13930,981070) == 0.005
    
