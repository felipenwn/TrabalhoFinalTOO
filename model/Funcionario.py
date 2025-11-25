class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def AtualizarCargo(self, novo_cargo, aumento_salario):
        self.cargo = novo_cargo
        self.salario  += aumento_salario

    def __str__(self):
        return f"Funcionario(nome={self.nome}, cpf={self.cpf}, salario={self.salario})" 