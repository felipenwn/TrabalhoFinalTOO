
class Consulta:
    def __init__(self, data, hora, descricao, animal, veterinario, status="Agendada"):
        self._data = data
        self._hora = hora
        self._descricao = descricao
        self._animal = animal
        self._veterinario = veterinario
        self._status = status
        self._observers = [] 
        
    @property
    def animal(self):
        return self._animal
    
    @property
    def veterinario(self):
        return self._veterinario
    
   
    def anexar(self, observer):
        """Adiciona um observador à lista."""
        if observer not in self._observers:
            self._observers.append(observer)

    def notificar(self):
        """Notifica todos os observadores sobre a mudança de estado."""
        for observer in self._observers:
            observer.atualizar(self)
        
    def agendarConsulta(self, data, hora, descricao):
        self._data = data
        self._hora = hora
        self._descricao = descricao
        self._status = "Agendada"
        self.notificar() 
        
    def cancelarConsulta(self):
        self._status = "Cancelada"
        self.notificar() 

    def finalizarConsulta(self):
        self._status = "Finalizada"
        self.notificar() 
        
    def __str__(self):
        return f"Consulta em {self._data} {self._hora}. Status: {self._status}. Vet: {self._veterinario.nome}"