from model.Tutor import Tutor
from model.Cachorro import Cachorro
from model.Gato import Gato
from model.Veterinario import Veterinario 
from model.Recepcionista import Recepcionista
from model.Consulta import Consulta


print("--- 1. HERANÇA: Criação de Objetos ---")
vet = Veterinario("Dr. Ricardo Santos", "123.456", 5000.00, "CRMV-100", "Clínico Geral")
recep = Recepcionista("Ana Silva", "789.012", 2000.00, "Manhã")


print(vet)
print(recep) 



print("\n--- 2. POLIMORFISMO: Emitir Som ---")
bichano = Gato("Félix", "Siamês", "2020-01-01", "Branco")
rex = Cachorro("Rex", "Pastor Alemão", "2018-05-15", "Preto e Marrom")

animais = [bichano, rex]
for animal in animais:
    print(f"{animal.nome} ({animal._especie}) diz: {animal.emitirSom()}") 




print("\n--- 3. ASSOCIAÇÃO: Tutor e Animal ---")
tutor = Tutor("Maria Oliveira", "111.222.333-44", "9999-8888", "Rua A")
tutor.adicionarAnimal(bichano)
tutor.adicionarAnimal(rex)
print(tutor)
print(f"Animais de Maria: {[a.nome for a in tutor.animais]}")



print("\n--- 4. ASSOCIAÇÃO e Fluxo ---")

consulta1 = Consulta("2025-11-25", "10:00", "Vacina de Rotina", rex, vet)
print(f"Status da consulta: {consulta1._status}")


vet.atenderConsulta(consulta1, "Animal saudável. Vacina aplicada.")
print(f"Novo status da consulta: {consulta1._status}")

rex.registrarConsulta(consulta1)
print(f"Consultas no prontuário do Rex: {len(rex.historico_consultas)}")