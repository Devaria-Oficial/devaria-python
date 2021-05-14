from classes.Animal import Animal

class Ave(Animal):
    def __init__(self, nome, qtdPenas, consegueVoar, consegueFazerMigracao):
        super().__init__(nome)
        self.qtdPenas = qtdPenas
        self.consegueVoar = consegueVoar
        self.consegueFazerMigracao = consegueFazerMigracao
