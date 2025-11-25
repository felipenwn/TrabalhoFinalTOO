from model.Animal import Animal
class Gato(Animal):
    def __init__(self, nome, raca, data_nascimento, cor):
        super().__init__(nome, "Gato", raca, data_nascimento, cor)

    def emitirSom(self):
        return "Miau!"