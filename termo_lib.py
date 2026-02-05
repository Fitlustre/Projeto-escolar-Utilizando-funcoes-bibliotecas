from random import choice
PALAVRAS = [
    "percurso", "detalhe", "memória", "contexto", "desafio",
    "recurso", "reflexão", "conceito", "impacto", "equilíbrio",
    "proposta", "iniciativa", "estrutura", "limite", "processo",
    "resposta", "solução", "elemento", "perspetiva", "objetivo",
    "estratégia", "relação", "função", "cenário", "dinâmica",
    "critério", "potencial", "influência", "resultado", "origem",
    "fator", "sequência", "noção", "evidência", "abordagem",
    "reação", "sentido", "base", "ligação", "etapa",
    "condição", "alternativa", "princípio", "controlo", "decisão",
    "adaptação", "evolução", "análise"
]
def palavra_aleatoria(): #Retorna uma palavra aleatoria
    return choice(PALAVRAS)

def palpite(palavra): #Compara o tamanho da de uma palavra com outra e devolve a palavra digitada
    cont = 0
    while True:
        palavra_esc = input('')
        if len(palavra_esc) != len(palavra):
            cont += 1
            print('Palavra inválida tete novamente!')
            if cont == 3:
                print(f'\033[33mDica: A palavra tem de conter {len(palavra)} letras.\033[m')
        else:
            break
    return palavra_esc


def comparar(palpite, palavra_certa): #Compara a palavra do palpite com a palavra certa e devolve o resultado colorido 
    lista=[]
    palavra = ''
    for c in range(len(palavra_certa)):
        lista.append(0)
    for pos, p in enumerate(palpite):
        if p == palavra_certa[pos]:
            lista[pos] = 1
        elif p in palavra_certa:
            lista[pos] = 2
        else:
            lista[pos] = 0

    for pos, l in enumerate(lista):
        if l == 1:
            palavra += f'\033[32m{palpite[pos]}\033[m'
        elif l == 2:
            palavra += f'\033[33m{palpite[pos]}\033[m'
        elif l == 0:
            palavra += f'\033[31m{palpite[pos]}\033[m'
    return palavra