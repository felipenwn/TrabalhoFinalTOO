# FuncionarioFactory.py

from model.Veterinario import Veterinario
from model.Recepcionista import Recepcionista

class FuncionarioFactory:

    @staticmethod
    def criar_funcionario(cargo, nome, cpf, salario, **kwargs):
        """
        Método estático para criar um objeto Funcionario.
        O 'kwargs' lida com os atributos específicos (crmv, especialidade, turno).
        """
        cargo_lower = cargo.lower()
        
        if cargo_lower == "veterinario":
            crmv = kwargs.get('crmv')
            especialidade = kwargs.get('especialidade')
            return Veterinario(nome, cpf, salario, crmv, especialidade)
            
        elif cargo_lower == "recepcionista":
            turno = kwargs.get('turno')
            return Recepcionista(nome, cpf, salario, turno)
            
        else:
            raise ValueError(f"Erro: Cargo '{cargo}' desconhecido.")