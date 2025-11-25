
class Consulta:
    def __init__(self, data, hora, descricao, animal, veterinario, status="Agendada"):
        self._data = data
        self._hora = hora
        self._descricao = descricao
        self._animal = animal
        self._veterinario = veterinario
        self._status = status
        
    @property
    def animal(self):
        return self._animal
    
    @property
    def veterinario(self):
        return self._veterinario
    
   
    def agendarConsulta(self, data, hora, descricao):
        self._data = data
        self._hora = hora
        self._descricao = descricao
        self._status = "Agendada"
        
    def cancelarConsulta(self):
        self._status = "Cancelada"

    def finalizarConsulta(self):
        self._status = "Finalizada"
        
    def __str__(self):
        return f"Consulta em {self._data} {self._hora}. Status: {self._status}. Vet: {self._veterinario.nome}"