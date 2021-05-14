from enums.MeioPagamento import MeioPagamento

class Pagamento:
    def __init__(self, meio_pagamento):
        self.meio_pagamento = meio_pagamento

    def RealizarPagamento(self, valor_compra):
        if(self.meio_pagamento == MeioPagamento.PIX):
            print(f'Pagamento R${valor_compra} com Pix realizado com sucesso!')
        elif (self.meio_pagamento == MeioPagamento.BOLETO):
            print(f'Pagamento R${valor_compra} com Boleto realizado com sucesso!')

