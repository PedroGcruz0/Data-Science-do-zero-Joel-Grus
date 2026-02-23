from typing import List
from collections import Counter

def raw_majority_vote(labels:List[str])-> str:
    #função para retornar o mais votado do Counter
    votes = Counter(labels)
    winner,_=votes.most_common(1)[0]
    return winner


# Bloco de testes
if __name__ == '__main__':
    #teste do mais votado
    assert raw_majority_vote(['a','b','c','b']) == 'b'
