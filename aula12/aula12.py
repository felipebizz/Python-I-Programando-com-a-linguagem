#Para isso realmente funcionar, devemos declarar o método como estático.
#O Python oferece para tal configuração um decorador. O decorador @staticmethod torna o método, um método da classe:

@staticmethod
def gerar_perfis(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    perfis = []
    for linha in arquivo:
        valores = linha.split(',')
        perfis.append(Perfil(*valores))
    arquivo.close()
    return perfis
