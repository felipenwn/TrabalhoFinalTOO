from model.Funcionario import Funcionario
from model.Animal import Animal
from model.Veterinario import Veterinario
from model.Recepcionista import Recepcionista
from model.Cachorro import Cachorro
from model.Gato import Gato
from model.Cavalo import Cavalo
from model.Tutor import Tutor
from model.Consulta import Consulta



# PILAR 1: ENCAPSULAMENTO

print("\n--- 1. ENCAPSULAMENTO (Proteção de Dados e Getters/Setters) ---")


tutor = Tutor("Carlos Silva", "333.333.333-33", "9876-5432", "Rua das Flores")
print(f"Objeto Tutor criado: {tutor._nome}")


print(f"Acessando nome (privado/protegido com '_'): {tutor._nome}")

print(f"Acessando nome (via Getter @property): {tutor.nome}")


tutor.atualizarDados(telefone="9999-1111")
print(f"Telefone atualizado via método público: {tutor._telefone}")

print("Conclusão: O encapsulamento foi demonstrado ao acessar o dado '_nome' via 'tutor.nome' (@property) e alterar o dado via 'atualizarDados()'.")



# PILAR 2: HERANÇA

print("\n--- 2. HERANÇA ('É UM') ---")


vet = Veterinario("Dr. Pedro Almeida", "111.111.111-11", 5000.00, "CRMV-200", "Ortopedia")
recep = Recepcionista("Juliana Costa", "222.222.222-22", 2000.00, "Tarde")

print(f"Objeto Veterinario (Filho) criado: {vet.nome}")
print(f"Objeto Recepcionista (Filho) criado: {recep.nome}")


print(f"Veterinário herdou o salário de Funcionário: R$ {vet.salario}")
print(f"Recepcionista herdou o salário de Funcionário: R$ {recep.salario}")


print(f"Veterinário tem atributo específico: Especialidade ({vet.especialidade})")
print(f"Recepcionista tem atributo específico: Turno ({recep._turno})")

print("Conclusão: As classes Veterinario e Recepcionista herdam atributos e métodos da classe Funcionario, demonstrando o conceito 'Veterinário É UM Funcionário'.")



# PILAR 3: POLIMORFISMO

print("\n--- 3. POLIMORFISMO ('Muitas Formas') ---")


rex = Cachorro("Rex", "Pastor", "2020-01-01", "Preto")
mimi = Gato("Mimi", "Persa", "2021-05-20", "Cinza")
spirit = Cavalo("Spirit", "Puro Sangue", "2019-03-01", "Marrom")

animais = [rex, mimi, spirit]


for animal in animais:
    print(f"{animal.nome} ({animal._especie}) emite o som: {animal.emitirSom()}")

print("Conclusão: O mesmo método (emitirSom) produz resultados diferentes dependendo do objeto (Cachorro, Gato, Cavalo), demonstrando Polimorfismo.")


# PILAR 4: ABSTRAÇÃO

print("\n--- 4. ABSTRAÇÃO (Classe Abstrata e Foco no Essencial) ---")


print("A classe Animal é Abstrata, pois define o contrato para suas subclasses.")


try:
    animal_generico = Animal("Generico", "N/A", "N/A", "2023-01-01", "N/A")
    print("ERRO: Conseguiu criar uma instância de Animal. A classe não está abstrata.")
except TypeError as e:

    if "Can't instantiate abstract class Animal with abstract method emitirSom" in str(e):
        print("SUCESSO: Tentativa de instanciar Animal falhou.")
        print(f"ERRO esperados: {e}")
    else:
        print(f"Erro inesperado: {e}")


print(f"O objeto Cachorro (Rex) foca na abstração 'Animal' (nome: {rex.nome}) mas implementa o detalhe 'emitirSom'.")
print("Conclusão: A classe Animal não pode ser instanciada diretamente e exige que as subclasses implementem 'emitirSom()', garantindo a Abstração.")
