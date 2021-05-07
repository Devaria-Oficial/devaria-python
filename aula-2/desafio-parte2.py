'''
    - Escrever um programa que recebe alguns produtos como argumento -- OK
    - Validar se esse produtos estão na lista de itens disponíveis do mercado -- OK
    - Caso esteja avisar o usuário quais produtos tem e quais não tem -- OK
    - E por ultimo exibir a lista de produtos disponíveis ordenados por ordem alfabética do mercado para que o usuário possa pedir na próxima vez -- OK
'''

if __name__ == '__main__':
    #Lista de produtos do usuário
    produtos_usuario = []

    #Lista de produtos disponíveis no mercado
    produtos_mercado = ['REFRIGERANTE', 'CERVEJA', 'MAÇÃ', 'PÃO']

    #Realiza a leitura dos produtos do usuário
    while True:
        produto = input("Digite um produto para adicionar na lista (Digite 'sair' para encerrar): ")

        if produto == 'sair':
            break

        if not produto.upper() in produtos_usuario:
            produtos_usuario.append(produto.upper())

    # Salvar produtos indisponíveis
    produtos_indisponiveis = []

    # Percorre a lista de produtos que o usuário digitou
    for p in produtos_usuario:

        # Valida se o produto está disponível ou não
        if not p.upper() in produtos_mercado:
            produtos_indisponiveis.append(p)

    print(f'Produtos indisponíveis: {produtos_indisponiveis}')

    #Ordenar lista de produtos disponíveis no mercado
    produtos_mercado.sort()
    print(f'Produtos disponíveis no Mercado: {produtos_mercado}')


