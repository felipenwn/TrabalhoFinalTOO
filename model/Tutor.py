class Tutor:
    def __init__(self, nome, cpf, telefone, endereco):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._endereco = endereco
        self._animais = []

    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
        
    @property
    def animais(self):
        return self._animais

    def adicionarAnimal(self, animal):
        self._animais.append(animal)
        

    def removerAnimal(self, animal_id):
        try:
            animal_removido = self._animais.pop(animal_id)
            return True
        except IndexError:
            print("Erro: Animal ID inválido.")
            return False

    def atualizarDados(self, nome=None, telefone=None, endereco=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone
        if endereco:
            self._endereco = endereco
            
    def atualizar(self, consulta):
        print(f" [Tutor: {self.nome}] NOTIFICAÇÃO: A consulta de {consulta.animal.nome} ({consulta._animal._especie}) foi '{consulta._status}'.") 

    def __str__(self):
        return f"Tutor: {self._nome} (CPF: {self._cpf}). Animais: {len(self._animais)}"