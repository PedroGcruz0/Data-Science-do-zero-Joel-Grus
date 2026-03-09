from typing import Set, NamedTuple, List, Tuple, Dict, Iterable
import re
import math
from collections import defaultdict


def tokenize (text:str) -> Set[str]:
    text = text.lower()
    all_words = re.findall("[a-z0-9']+", text) #busco usando o regex
    return set(all_words)#adiciono no set 

class Message(NamedTuple):
    text: str
    is_spam:bool

    
class NaiveBayesClassifier:
    def __init__(self, k:float = 0.5) -> None:
        self.k = k
        self.tokens : Set[str] = set()
        self.token_spam_counts: Dict[str,int] = defaultdict(int)
        self.token_ham_counts: Dict[str, int] = defaultdict(int)
        self.spam_messages = self.ham_messages = 0


    def train(self, messages: Iterable[Message]) -> None:
        for message in messages:
            #Incrementar a contagem das mensagens
            if message.is_spam:
                self.spam_messages +=1
            else:
                self.ham_messages +=1

            #Incrementar a contagem de palavras
            for token in tokenize(message.text):
                self.tokens.add(token)
                if message.is_spam:
                    self.token_spam_counts[token]+=1
                else:
                    self.token_ham_counts[token]+=1

    def _probabilities(self,token:str) -> Tuple [float,float]:
        """Retorna a P(token|ham) de cada token do vocabulario"""
        spam = self.token_sepam_counts[token]
        ham = self.token_ham_counts[token]

        p_token_spam = (spam +self.k)/(self.spam_messages + 2*self.k)
        p_token_ham = (ham + self.k)/(self.ham_messages +2*self.k)
        return p_token_spam,p_token_ham
    
    def predict(self, text: str) -> float:
        # Aí usamos os logarítmos pois se multiplicarmos as probabilidades elas vão ficar menor do que o computador consegue identificar
        text_tokens = tokenize(text)
        log_prob_if_spam = log_prob_if_ham = 0.0

        # Iteramos por todas as palavras que o modelo conhece
        for token in self.tokens:
            prob_if_spam, prob_if_ham = self._probabilities(token)

            # Se a palavra está na mensagem somamos log(P)
            if token in text_tokens:
                log_prob_if_spam += math.log(prob_if_spam)
                log_prob_if_ham += math.log(prob_if_ham)
            
            # Se a palavra não está na mensagem, somamos log(1 - P)
            else:
                log_prob_if_spam += math.log(1.0 - prob_if_spam)
                log_prob_if_ham += math.log(1.0 - prob_if_ham)
                
        # Transformar Log de volta em Probabilidade (0 a 1)
        prob_if_spam = math.exp(log_prob_if_spam)
        prob_if_ham = math.exp(log_prob_if_ham)
        
        return prob_if_spam / (prob_if_spam + prob_if_ham)
            


if __name__ == '__main__':
    assert tokenize ("Data science is science")== {"data","science","is"}

