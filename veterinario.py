
from model.Funcionario import Funcionario

class Veterinario(Funcionario):
    def __init__(self,nome,cpf,salario,crmv,especialidade):
        super().__init__(nome,cpf,salario)
        self.crmv = crmv
        self.especialidade = especialidade
