from model.Funcionario import Funcionario

class Veterinario(Funcionario):

    def __init__(self, nome, cpf, salario, crmv, especialidade):
        super().__init__(nome, cpf, salario)
        self._crmv = crmv
        self._especialidade = especialidade
        

    @property
    def crmv(self):
        return self._crmv
    
    @property
    def especialidade(self):
        return self._especialidade


    def atenderConsulta(self, consulta, diagnostico):
        consulta.finalizarConsulta()
        print(f"Dr(a). {self.nome} atendeu a consulta. Diagnóstico: {diagnostico}")
        

    def atualizarEspecialidade(self, nova_especialidade):
        self._especialidade = nova_especialidade
        
    def __str__(self):
        return f"Veterinario(nome={self.nome}, crmv={self._crmv}, especialidade={self._especialidade})"