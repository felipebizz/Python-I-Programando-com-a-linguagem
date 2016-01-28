
#Abra a classe Perfil e adicione no método gerar_perfis a verificação (if):

@staticmethod
def gerar_perfis(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    perfis = []
    for linha in arquivo:
        valores = linha.split(',')
        if(len(valores) is not 3):
            raise PerfilErro('Uma linha no arquivo deve ter 3 valores') #lançando PerfilError
        perfis.append(Perfil(*valores))
    arquivo.close()
    return perfis


    class PerfilErro(Exception):
    def __init(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return repr(self.mensagem)
