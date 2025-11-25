
from model.Funcionario import Funcionario

class Recepcionista(Funcionario):

    def __init__(self, nome, cpf, salario, turno):
        super().__init__(nome, cpf, salario)
        self._turno = turno 


    def agendar_consulta(self, animal, veterinario, data, hora, descricao):
        print(f"Recepcionista {self.nome} agendou: {animal.nome} com Dr. {veterinario.nome}")
        
    def __str__(self):
        return f"Recepcionista(nome={self.nome}, turno={self._turno})"