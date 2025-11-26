# AnimalFactory.py

from model.Cachorro import Cachorro
from model.Gato import Gato
from model.Cavalo import Cavalo

class AnimalFactory:
    @staticmethod
    def criar_animal(tipo, nome, raca, data_nascimento, cor):
        tipo_lower = tipo.lower()
        
        if tipo_lower == "cachorro":
        
            return Cachorro(nome, raca, data_nascimento, cor)
        elif tipo_lower == "gato":
        
            return Gato(nome, raca, data_nascimento, cor)
        elif tipo_lower == "cavalo":
        
            return Cavalo(nome, raca, data_nascimento, cor)
        else:
            raise ValueError(f"Erro: Tipo de animal '{tipo}' desconhecido.")