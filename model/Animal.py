class Animal:
    def __init__(self, nome, especie, raça, data_nascimento, cor):
        self.nome = nome
        self.especie = especie
        self.raça = raça
        self.data_nascimento = data_nascimento
        self.cor = cor

    def atualizarInformacoes(self, nome=None, especie=None, raça=None, data_nascimento=None, cor=None):
            if nome:
                self.nome = nome
            if especie:
                self.especie = especie
            if raça:
                self.raça = raça
            if data_nascimento:
                self.data_nascimento = data_nascimento
            if cor:
                self.cor = cor

    def registrarConsulta(self, data_consulta, motivo, veterinario):
        consulta = {
            "data_consulta": data_consulta,
            "motivo": motivo,
            "veterinario": veterinario
        }
        return consulta
    
    def emitirSom(self):
        return "Som genérico de animal"