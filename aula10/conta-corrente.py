class ContaCorrente(Conta):
    def __init__(self, titular, saldo):
        super(ContaCorrente, self).__init__(titular, saldo)
    def calcular_imposto(self):
        return super(ContaCorrente, self).calcular_imposto() + 20
