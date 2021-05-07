class ContaBancaria:
    def __init__(self, tipo, conta, agencia):
        self.tipo = tipo
        self.conta = conta
        self.agencia = agencia

    def exibirDadosDaConta(self):
        print(f'Informações da Conta: Tipo: {self.tipo} - Conta: {self.conta} - Agencia: {self.agencia}')

if __name__ == '__main__':
    conta1 = ContaBancaria('corrente', 6548, '57002')
    conta1.exibirDadosDaConta()


    conta1.tipo = 'poupança'
    conta1.exibirDadosDaConta()


    conta2 = ContaBancaria('conjunta', 3449, '97889')
    conta2.exibirDadosDaConta()



