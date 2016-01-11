# -*- coding: UTF-8 -*-

class Data():
    'Retorna data formatada'
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def imprime_data_formatada(self):
        print(" %s/%s/%s" % (self.dia, self.mes, self.ano))
