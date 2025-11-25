class Funcionario:
    def __init__(self, nome, cpf, salario):

        self._nome = nome
        self._cpf = cpf
        self._salario = salario

  
    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario
    
 
    def AtualizarCargo(self, novo_cargo):
        self._cargo = novo_cargo


    def calcularSalario(self):
        return self._salario
    
    def __str__(self):
        return f"Funcionario(nome={self._nome}, cpf={self._cpf}, salario={self._salario})"