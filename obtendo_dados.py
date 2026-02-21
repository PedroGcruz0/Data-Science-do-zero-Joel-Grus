import sys
import csv
from typing import List, Dict, Callable
from collections import Counter

#ler arquivos de texto
def ler_arquivo_completo(nome_arquivo:str) -> str:
    #lê o arquivo inteiro e retorna em String única """assim"""
    with open (nome_arquivo,'r') as f:
        return f.read()
    
def ler_linhas_arquivo(nome_arquivo:str) -> List[str]:
    #lê um arquivo e retorna onde cada linha é um item
    with open(nome_arquivo, 'r') as f:
        return [line.strip() for line in f]
        # strip() remove o \n do final

def ler_csv_como_lista(nome_arquivo:str, delimitador:str =',') -> List[List[str]]:
    """
    Lê um CSV e retorna uma lista de listas.
    Ex: [['Nome', 'Idade'], ['Pedro', '30'], ['Maria', '25']]
    """
    with open(nome_arquivo, 'r') as f:
        reader = csv.reader(f, delimiter=delimitador)
        return [row for row in reader]
    
def leia_csv_como_dict(nome_arquivo: str, delimitador: str = ',') -> List[Dict[str, str]]:
    """
    Lê um CSV e retorna uma lista de dicionários (mais seguro).
    Ex: [{'Nome': 'Pedro', 'Idade': '30'}, ...]
    """
    with open(nome_arquivo, 'r') as f:
        reader = csv.DictReader(f, delimiter=delimitador)
        return [row for row in reader]
    
def escreva_csv(nome_arquivo: str, data: List[List[str]], delimitador: str = ','):
    """Escreve uma lista de listas em um arquivo CSV."""
    with open(nome_arquivo, 'w', newline='') as f: # 'w' = write (escrever)
        writer = csv.writer(f, delimiter=delimitador)
        for row in data:
            writer.writerow(row)

def count_stdin_lines():
    """
    Conta linhas que vêm do 'input padrão' (stdin).
    Isso permite usar o pipe no terminal: cat arquivo.txt | python getting_data.py
    """
    count = 0
    for line in sys.stdin:
        count += 1
    return count

def most_common_words_stdin(n: int = 10):
    """Conta as palavras mais comuns vindas do stdin"""
    counter = Counter()
    for line in sys.stdin:
        # Quebra a linha em palavras (minúsculas)
        words = line.strip().lower().split()
        for word in words:
            if word:
                counter[word] += 1

    # Imprime o resultado no stdout
    for word, count in counter.most_common(n):
        sys.stdout.write(f"{word}\t{count}\n")


#BLOCO DE TESTE

if __name__ == "__main__":
    
    # Exemplo de uso de argumentos da linha de comando (sys.argv)
    # Ex: python getting_data.py --count
    
    if len(sys.argv) > 1 and sys.argv[1] == "--count":
        print("Contando linhas do que você digitar (Ctrl+D para encerrar)...")
        qtd = count_stdin_lines()
        print(f"Total de linhas: {qtd}")
        
    elif len(sys.argv) > 1 and sys.argv[1] == "--words":
        print("Contando palavras do que você digitar...")
        most_common_words_stdin()
        
    else:
        dados_fake = [['Nome', 'Nota'], ['Ana', '10'], ['Beto', '8']]
        escreva_csv('notas_teste.csv', dados_fake)
        
        print("Arquivo 'notas_teste.csv' criado.")
        
        # Agora vamos ler de volta
        lido = leia_csv_como_dict('notas_teste.csv')
        print("Lendo o arquivo de volta como dicionário:")
        for linha in lido:
            print(linha)