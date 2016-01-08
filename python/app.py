# -*- coding: UTF-8 -*-

def listar(nomes):
    print ('Listando Nomes: ')
    for nome in nomes:
        print(nome)


def cadastrar (nomes) :
    print ('Digite seu Nome :')
    nome = raw_input()
    nomes.append(nome)

def remover (nomes):
    print('Qual nome Gostaria de remover ? ')
    nome_a_remover = raw_input()
    nomes.remove(nome_a_remover)
    listar(nomes)

def alterar(nomes):
    print ('Qual nome gostaria de alterar?')
    nome_a_alterar = raw_input()
    index = nomes.index(nome_a_alterar)
    print ('Digite o novo nome: ')
    nome_alterado = raw_input()
    nomes[int(index)] = nome_alterado

def procurar(nomes):
    print ('Digite o nome a procurar')
    nome_a_procurar = raw_input()
    if (nome_a_procurar in nomes):
        print('Nome encontrado com sucesso')
    else:
        print('Nome nao existe')

def menu ( ):
    nomes = []
    escolha = ' '
    while (escolha != '0'):
        print ('Digite 1 para cadastrar')
        print ('Digite 2 para Listar')
        print ('Digite 3 para remover')
        print ('Digite 4 para alterar')
        print ('Digite 5 para procurar')
        print ('Digite 0 para terminar')

        escolha =  raw_input()

        if (escolha == '1'):
            cadastrar (nomes)
        if(escolha == '2'):
            listar(nomes)
        if(escolha == '3'):
            remover(nomes)
        if(escolha == '4'):
            alterar(nomes)
        if(escolha == '5'):
            procurar(nomes)

menu()
