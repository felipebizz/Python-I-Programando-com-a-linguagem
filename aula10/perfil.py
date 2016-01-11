# -*- coding: UTF-8 -*-
class Perfil(object):
    'Classe padrão para perfis de usuários'
    def __init__(self, nome, telefone, empresa, tipo):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0
        self.__tipo = tipo

    def imprimir(self):
        print "Nome : %s, Telefone: %s, Empresa %s" % (self.nome, self.telefone, self.empresa)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    def obter_creditos(self):
        if self.__tipo == 1:
            return self.__curtidas * 10.0

    def obter_tipo(self):
        return self.__tipo    
