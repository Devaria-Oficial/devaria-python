from classes.Animal import Animal


class Peixe(Animal):
    def __init__(self, nome, qtdNadadeiras, isPeixeAguaSalgada, isCarnivoro):
        super().__init__(nome)
        self.qtdNadadeiras = qtdNadadeiras
        self.isPeixeAguaSalgada = isPeixeAguaSalgada
        self.isCarnivoro = isCarnivoro

    def nadar(self):
        print(f'O peixe {self.nome} está nadando.')