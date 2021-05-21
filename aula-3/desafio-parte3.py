'''
    1. Escrever um programa que recebe os produtos a serem comprados - OK
    2. A forma de pagamentos escolhida - OK
    3. De acordo com a forma de pagamento efetuar a compra utilizando o correto meio de pagamento. - OK
'''
from classes.Compra import Compra
from enums.MeioPagamento import MeioPagamento

if __name__ == '__main__':
    produtos_disponiveis = [
        {'nome': 'Chinelo', 'preco_unidade': 20},
        {'nome': 'Tenis', 'preco_unidade': 250},
        {'nome': 'Sandália', 'preco_unidade': 100},
        {'nome': 'Calça', 'preco_unidade': 120}
    ]

    produtos_selecionados = []

    while True:
        produto_digitado = input("Digite o nome do produto que irá comprar ('sair' para sair): ")

        if(produto_digitado == 'sair'):
            break

        produtos_encontrados = list(filter(lambda p : p['nome'] == produto_digitado, produtos_disponiveis))

        if len(produtos_encontrados) == 0:
            print('Esse produto não foi encontrado, favor digitar outro.')
        else:
            while True:
                try:
                    qtd_produto = int(input(f"Digite a quantidade de {produto_digitado} que você deseja: "))
                    break
                except:
                    print('Quantidade digitada incorreta, favor digitar novamente.')

            produtos_selecionados.append({
                'nome': produto_digitado,
                'quantidade': qtd_produto,
                'valor': produtos_encontrados[0]['preco_unidade']
            })

    while True:
        try:
            meio_pagamento_digitado = input(f'Digite a forma de Pagamento ({MeioPagamento.PIX.value} ou {MeioPagamento.BOLETO.value}): ')
            meio_pagamento = MeioPagamento(meio_pagamento_digitado)
            break
        except:
            print("Forma de pagamento inválida, favor digitar novamente.")

    compra = Compra(meio_pagamento, produtos_selecionados)
    compra.RealizarCompra()




