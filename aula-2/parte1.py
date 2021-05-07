def lavarCarro(posicao):
    print(f'Lavando carro na posicao {posicao}...')

def verificarTemCarroNaFila(posicao):
    if(posicao > 5):
        return False
    else:
        return True


if __name__ == '__main__':

    n = 1
    print(f'Linha {n}')
    n += 1
    print(f'Linha {n}')
    n += 1
    print(f'Linha {n}')
    n += 1
    print(f'Linha {n}')


    #Estrutura de repetição com intervalo de valores
    ##For Crescente
    print('For Crescente')
    for n in range(0, 5):
        print(n)

    ##For Descrente
    print('For Decrescente')
    for n in range(5, 0, -1):
        print(n)

    ##For percorrendo caracteres de uma String
    print('For percorrendo String')
    palavra = 'Devaria'
    for p in palavra:
        print(p)

    ## Estrutura de repetição While crescente
    print('While crescente')
    n = 0
    while n < 5:
        print(n)
        n += 1

    ## Estrutura de repetição com While
    temCarroNaFila = True
    posicao = 1
    while temCarroNaFila:
        lavarCarro(posicao)
        posicao += 1
        temCarroNaFila = verificarTemCarroNaFila(posicao)
    else:
        print('Terminou de lavar os carros!')



