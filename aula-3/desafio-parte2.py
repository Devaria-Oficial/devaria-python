'''
    1. Escrever um programa que recebe um nome de animal vertebrado - OK
    2. De acordo com um filtro identifica qual dos grupos ele pertence (Mamífero, Réptil, Ave e Peixe) - OK
    3. Exibir os dados genéricos e exclusivos de cada grupo de animal - OK
'''
from classes.Ave import Ave
from classes.Mamifero import Mamifero
from classes.Peixe import Peixe
from classes.Reptil import Reptil

import abc

if __name__ == '__main__':
    lista_animais = [
        Mamifero('Leão', 4, False, False),
        Reptil('Serpente', 4, True, 0),
        Ave('Gavião', 500, True, False),
        Peixe('Tubarão', 2, True, True)
    ]

    nome_animal = input("Digite o nome do Animal: ")

    animal_encontrado = list(filter(lambda a : a.nome == nome_animal, lista_animais))

    if len(animal_encontrado) == 0:
        print('Animal não encontrado')
    else:
        try:
            if(isinstance(animal_encontrado[0], Mamifero)):
                animal_encontrado[0].Respirar()
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Mamífero, qtdMamas: {animal_encontrado[0].qtdMamas}')
            elif(isinstance(animal_encontrado[0], Ave)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Ave, qtdPenas: {animal_encontrado[0].qtdPenas}')
            elif (isinstance(animal_encontrado[0], Peixe)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Peixe, qtdNadadeiras: {animal_encontrado[0].qtdNadadeiras}')
            elif (isinstance(animal_encontrado[0], Reptil)):
                print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Reptil, temperaturaCorporal: {animal_encontrado[0].temperaturaCorporal}')
            else:
                print('Ocorreu um erro ao definir o tipo do animal.')
        except Exception as e:
            print('Ocorreu um erro, favor tentar novamente.')




