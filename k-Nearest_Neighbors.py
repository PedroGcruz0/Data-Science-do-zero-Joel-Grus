from typing import List
from collections import Counter

def raw_majority_vote(labels:List[str])-> str:
    #função para retornar o mais votado do Counter
    votes = Counter(labels)
    winner,_=votes.most_common(1)[0]
    return winner


def majority_vote(labels:List[str])->str:
    """supõe que os blocos estão classificados do mais próximo ao mais distânte"""
    vote_counts = Counter(labels)
    #o most common retorna um dict de prinetiro colocado e os votos, pego só o primeiro colocado e os votos
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winner = len([count for count in vote_counts.values()
                      if count == winner_count])
    if num_winner == 1:
        return winner
    
    else:
        return majority_vote(labels[:-1]) #tenta novamente sem o mais distante
    
# Bloco de testes
if __name__ == '__main__':
    #teste do mais votado
    assert raw_majority_vote(['a','b','c','b']) == 'b'
    assert majority_vote(['a','b','c','b', 'a']) == 'b'

