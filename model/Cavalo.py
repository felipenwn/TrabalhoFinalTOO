from model.Animal import Animal
class Cavalo(Animal):
    def __init__(self, nome, raca, data_nascimento, cor):
        super().__init__(nome, "Cavalo", raca, data_nascimento, cor)

    def emitirSom(self):
        return "Relincho!"