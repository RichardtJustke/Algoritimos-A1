```md
# 🐍 Projetos em Python – Fundamentos de Programação

Este repositório reúne todos os projetos e exercícios desenvolvidos durante o estudo de **lógica de programação em Python**. Ele inclui tanto exercícios individuais de cada conteúdo quanto um projeto prático completo (o Mercadinho), que une todos esses conceitos em um único sistema funcional.

A proposta deste repositório é mostrar, na prática, como os principais fundamentos da programação funcionam juntos dentro de um programa real.

---

## 📁 Estrutura do Repositório

A organização dos arquivos foi feita por conteúdo, da seguinte forma:

```

A1-Algoritmos/
├── condicionais/
│   └── verificacao_idade.py
├── repeticao/
│   └── pares_1_a_100.py
├── listas/
│   └── lista_alunos.py
├── dicionarios/
│   └── cadastro_produtos.py
├── mercadinho.py
└── README.md

````

Cada pasta representa um conteúdo específico estudado, além do projeto final que une tudo.

---

## ✅ Conteúdos e Projetos

### 1️⃣ Estruturas Condicionais – Verificação de Idade  
Arquivo: `condicionais/verificacao_idade.py`  

Programa que solicita a idade do usuário e informa se ele pode ou não entrar em um evento.  
Neste exercício foi praticado:
- Uso de `if`, `elif` e `else`
- Entrada de dados com `input`
- Tomada de decisão no sistema

Execução:
```bash
python condicionais/verificacao_idade.py
````

---

### 2️⃣ Estruturas de Repetição – Números Pares de 1 a 100

Arquivo: `repeticao/pares_1_a_100.py`

Programa que exibe todos os números pares de 1 até 100 utilizando dois tipos de laços:

* `for`
* `while`

Neste exercício foi praticado:

* Laços de repetição
* Operadores matemáticos
* Controle de fluxo

Execução:

```bash
python repeticao/pares_1_a_100.py
```

---

### 3️⃣ Listas – Cadastro de Alunos

Arquivo: `listas/lista_alunos.py`

Programa que permite cadastrar nomes de alunos em uma lista e exibe todos ao final.
O usuário pode digitar "sair" para encerrar a entrada de dados.

Neste exercício foi praticado:

* Uso de listas
* Entrada dinâmica de dados
* Laço de repetição para leitura contínua

Execução:

```bash
python listas/lista_alunos.py
```

---

### 4️⃣ Dicionários – Cadastro de Produtos

Arquivo: `dicionarios/cadastro_produtos.py`

Sistema simples de cadastro de produtos utilizando um dicionário para armazenar nome e preço.

Neste exercício foi praticado:

* Uso de dicionários
* Organização de dados por chave e valor
* Exibição dos dados cadastrados

Execução:

```bash
python dicionarios/cadastro_produtos.py
```

---

## 🛒 Projeto Final – Mercadinho em Python

Arquivo: `mercadinho.py`

Este projeto simula um pequeno mercado funcionando no terminal. Ele foi criado para unir todos os conceitos estudados em um único sistema prático e funcional.

O mercadinho permite:

* Cadastrar produtos (nome e preço)
* Listar os produtos cadastrados
* Simular uma compra com vários produtos
* Calcular e exibir o total da compra
* Navegar por um menu interativo no terminal

A ideia do projeto é sair dos exercícios isolados e aplicar tudo em uma situação real de uso.

---

## 🧱 Organização dos Dados no Mercadinho

Os produtos são armazenados dentro de uma lista, onde cada item é um dicionário com nome e preço:

```python
[
  {"nome": "Arroz", "preco": 25.0},
  {"nome": "Feijão", "preco": 9.5}
]
```

---

## ▶️ Como Executar o Mercadinho

```bash
python mercadinho.py
```

Ao executar, o menu aparece automaticamente no terminal:

```
=== MERCADINHO DO JUSTKE 💸 ===
1 - Cadastrar produto
2 - Listar produtos
3 - Comprar produtos
4 - Sair
```

O usuário navega pelo sistema digitando apenas os números das opções.

---

## 🧠 Conceitos Trabalhados no Repositório

Ao longo de todos os arquivos, foram utilizados:

* Listas
* Dicionários
* Estruturas condicionais (`if`, `elif`, `else`)
* Laços de repetição (`for`, `while`)
* Entrada de dados (`input`)
* Conversão de tipos (`int`, `float`)
* Validação de dados
* Lógica para soma e controle de fluxo

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Terminal
* Git
* GitHub

---

## 🎯 Objetivo do Repositório

Este repositório tem como objetivo fortalecer a base da programação em Python, passando por cada conceito separadamente e depois aplicando tudo em um projeto completo.

Ele representa a transição do aprendizado teórico para a prática real, com sistemas funcionando de verdade.

```


