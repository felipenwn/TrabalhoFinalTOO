# 📄 Roteiro: Sistema de Gestão para Clínica Veterinária

## 1. Introdução e Visão Geral do Projeto

### 1.1. Tema e Objetivo

Este projeto simula um **Sistema de Gestão para Clínica Veterinária**, aplicando os conceitos fundamentais da Programação Orientada a Objetos para modelar entidades do mundo real como classes, atributos e relacionamentos.

O objetivo principal é demonstrar o domínio sobre os **Quatro Pilares da disciplina de TOO**: Encapsulamento, Herança, Polimorfismo e Abstração, na construção de um sistema modular.

### 1.2. Tecnologias Utilizadas
* **Linguagem de Programação:** Python
* **Paradigma:** Programação Orientada a Objetos (POO)
* **Ferramentas:** Diagrama UML (para modelagem)

***

## 2. Arquitetura do Sistema: Diagrama UML

O sistema foi modelado utilizando o Diagrama de Classes UML (Unified Modeling Language), que define a estrutura estática do projeto, as classes, seus atributos, métodos e as relações entre elas.

**Estrutura Principal:**
* **Hierarquia de Animais:** `Animal` (Abstrata) -> `Cachorro`, `Gato`, `Cavalo`.
* **Hierarquia de Funcionários:** `Funcionario` -> `Veterinario`, `Recepcionista`.
* **Associações Centrais:** `Tutor` se associa a `Animal`; `Consulta` se associa a `Animal` e a `Veterinario`.

### 2.1. Diagrama de Classes UML

![imagem-UML](<./TrabalhoFinalTOO/src/img/Diagrama UML.jpg>)

***

## 3. Descrição Detalhada das Classes

### A. Classes de Funcionários (Hierarquia de Herança)

| Classe | Descrição | Atributos (Principais) | Métodos (Principais) |
| :--- | :--- | :--- | :--- |
| **`Funcionario`** | Superclasse que representa qualquer colaborador da clínica. | `nome`, `cpf`, `salario`. | `calcularSalario()`. |
| **`Veterinario`** | Subclasse de `Funcionario`. Responsável por atendimentos e diagnósticos. | *Herda de Funcionario*, `crmv`, `especialidade`. | `atenderConsulta(consulta, diagnostico)`, `atualizarEspecialidade()`. |
| **`Recepcionista`** | Subclasse de `Funcionario`. Responsável por tarefas administrativas e agendamento. | *Herda de Funcionario*, `turno`. | `agendar_consulta()`. |

### B. Classes de Pacientes (Hierarquia de Polimorfismo)

| Classe | Descrição | Atributos (Principais) | Métodos (Principais) |
| :--- | :--- | :--- | :--- |
| **`Animal`** | **Classe Abstrata.** Define o contrato base para todos os pacientes. Contém o prontuário. | `nome`, `raca`, `data_nascimento`, `_historico_consultas`. | `emitirSom()` (Abstrato), `registrarConsulta(consulta)`. |
| **`Cachorro`** | Subclasse de `Animal`. | *Herda de Animal*. | `emitirSom()` (implementa 'Au Au!'). |
| **`Gato`** | Subclasse de `Animal`. | *Herda de Animal*. | `emitirSom()` (implementa 'Miau!'). |
| **`Cavalo`** | Subclasse de `Animal`. | *Herda de Animal*. | `emitirSom()` (implementa 'Relincho!'). |

### C. Classes de Suporte

| Classe | Descrição | Atributos (Principais) | Métodos (Principais) |
| :--- | :--- | :--- | :--- |
| **`Tutor`** | Representa o cliente e dono dos animais. | `nome`, `cpf`, `telefone`, `_animais` (Lista de objetos `Animal`). | `adicionarAnimal()`, `removerAnimal()`, `atualizarDados()`. |
| **`Consulta`** | Representa o evento do atendimento. Associa o `Animal` ao `Veterinario`. | `data`, `hora`, `descricao`, `status`, `_animal`, `_veterinario`. | `agendarConsulta()`, `cancelarConsulta()`, `finalizarConsulta()`. |

***

## 4. Os Quatro Pilares da Programação Orientada a Objetos

O projeto foi estruturado para destacar a aplicação prática dos quatro pilares essenciais da POO.

### 4.1. Encapsulamento (Encapsulation)

O Encapsulamento protege os dados internos de um objeto, controlando o acesso e a modificação de seus atributos.

**Aplicação no Projeto:**
* Atributos Protegidos (ex: `_nome`, `_salario`).
* Acesso via Getters (`@property`) e modificação via métodos públicos (ex: `Tutor.atualizarDados()`).

**Exemplo de Código:**

[INSIRA O TRECHO DE CÓDIGO DO GETTER (@property) EM Tutor.py AQUI]

### 4.2. Herança (Inheritance)

A Herança permite que uma nova classe (subclasse) herde atributos e métodos de uma classe existente (superclasse), promovendo a reutilização de código e definindo relações "É UM".

**Aplicação no Projeto:**
* `Veterinario` e `Recepcionista` **herdam** de `Funcionario`.
* `Cachorro`, `Gato` e `Cavalo` **herdam** de `Animal`.

**Exemplo de Código:**

[INSIRA O TRECHO DE CÓDIGO DE super().__init__(...) NA CLASSE Veterinario.py AQUI]

### 4.3. Polimorfismo (Polymorphism)

O Polimorfismo permite que objetos de diferentes classes respondam de maneiras distintas ao mesmo comando ou método, através da sobrescrita (override) de métodos.

**Aplicação no Projeto:**
* O método `emitirSom()` é definido em `Animal` e **sobrescrito** em cada subclasse (`Cachorro`, `Gato`, `Cavalo`), gerando resultados diferentes para a mesma chamada.

**Exemplo de Código:**

[INSIRA O TRECHO DE CÓDIGO DA IMPLEMENTAÇÃO DE emitirSom() NA CLASSE Cachorro.py AQUI]

### 4.4. Abstração (Abstraction)

A Abstração foca apenas nos aspectos essenciais de um objeto, escondendo a complexidade desnecessária e definindo um contrato para as classes filhas.

**Aplicação no Projeto:**
* **Classe Abstrata `Animal`:** Não pode ser instanciada diretamente.
* **Método Abstrato:** O método `emitirSom()` é definido como **abstrato**, forçando as subclasses a implementá-lo.

**Exemplo de Código:**

[INSIRA O TRECHO DE CÓDIGO DA CLASSE Animal.py DEMONSTRANDO ABC E @abstractmethod AQUI]

***

## 5. Demonstração de Execução

[INSIRA A IMAGEM OU TRECHO DE CÓDIGO DA EXECUÇÃO DO SEU ARQUIVO DE TESTE (test_pilares_poo.py) AQUI]
