# -*- coding: UTF-8 -*-

class Pessoa():
    'Calculo de IMC'
    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprime_imc(self):
        imc = (self.peso / (self.altura * self.altura))
        print(" %s,  seu IMC é: %s" % (self.nome, imc))
