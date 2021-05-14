from classes.Animal import Animal

class Mamifero(Animal):
    def __init__(self, nome, qtdMamas, isMamiferoAquatico, consegueBotarOvo):
        super().__init__(nome)
        self.qtdMamas = qtdMamas
        self.isMamiferoAquatico = isMamiferoAquatico
        self.consegueBotarOvo = consegueBotarOvo

