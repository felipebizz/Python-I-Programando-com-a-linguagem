from datetime import date

def cadastrar(nomes) :
    print 'Digite o nome: '
    nome = raw_input()
    nomes.append(nome)

def calculaIdade()
    ano_como_string = raw_input()
    ano = int(ano_como_string)
    ano_atual = date.today().year
    ano_atual - ano

def remover(nomes):
    print 'Qual nome você gostaria de remover?'
    nome_a_remover = raw_input()
    nomes.remove(nome_a_remover)
    nomes
