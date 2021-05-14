from classes.Pagamento import Pagamento


class Compra(Pagamento):
    def __init__(self, meio_pagamento, produtos):
        super().__init__(meio_pagamento)
        self.produtos = produtos

    def __calcularValorCompra(self):
        valor_compra = 0

        for p in self.produtos:
            valor_compra += p['valor'] * p['quantidade']

        return valor_compra

    def RealizarCompra(self):
        valor_compra = self.__calcularValorCompra()

        self.RealizarPagamento(valor_compra)
