from abc import ABC, abstractmethod
from .Consulta import Consulta

class Animal(ABC):
    def __init__(self, nome, especie, raca, data_nascimento, cor):

        self._nome = nome
        self._especie = especie
        self._raca = raca
        self._data_nascimento = data_nascimento
        self._cor = cor
        self._historico_consultas = [] 


    @property
    def nome(self):
        return self._nome
    
    @property
    def historico_consultas(self):
        return self._historico_consultas

    def atualizarInformacoes(self, nome=None, especie=None, raca=None, data_nascimento=None, cor=None):
            if nome:
                self._nome = nome
            if especie:
                self._especie = especie
            if raca:
                self._raca = raca
            if data_nascimento:
                self._data_nascimento = data_nascimento
            if cor:
                self._cor = cor


    def registrarConsulta(self, consulta):
        self._historico_consultas.append(consulta)
    
 
    @abstractmethod
    def emitirSom(self):
        pass

    def __str__(self):
        return f"Animal: {self._nome} ({self._especie}/{self._raca})"
