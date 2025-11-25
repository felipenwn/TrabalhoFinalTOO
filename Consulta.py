class Consulta:
    def __init__(self,data,hora,descricao,status):
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.status = status

    def agendarConsulta(self,data,hora,descricao):
        self.data = data
        self.hora = hora
        self.descricao = descricao
        self.status = "Agendada"
        
    def cancelarConsulta(self):
        self.status = "Cancelada"

    def finalizarConsulta(self):
        self.status = "Finalizada" 