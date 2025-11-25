
from model.Animal import Animal
class Cachorro(Animal):
    def __init__(self, nome, raca, data_nascimento, cor):
        super().__init__(nome, "Cachorro", raca, data_nascimento, cor)

    def emitirSom(self):
        return "Au Au!"
    

