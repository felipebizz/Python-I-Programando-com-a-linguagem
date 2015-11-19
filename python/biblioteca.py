from aula4.aula4 import nome


def gera_nome_convite(convite):
    posicao_final = len(convite)
    posicao_inicial = posicao_final - 4
    parte1 = convite[0:6]
    parte2 = convite[posicao_inicial : posicao_final]
    print(posicao_inicial)
    print(parte2)
    return parte1 +' '+ parte2

def envia_convite(nome_convidado):
    print("Enviando convite para : ", (nome_convidado))


def processa_convite(nome_convidado):
    nome_gerado = gera_nome_convite(nome_convidado)
    envia_convite(nome_gerado)
