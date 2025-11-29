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

Boa — vamos **dar um upgrade só na parte do Mercadinho**, deixando mais clara, mais madura e sem blá blá blá, do jeito que tu pediu 😎
👉 **Substitui APENAS a seção do Mercadinho no teu README por esta aqui abaixo:**

````md
## 🛒 Projeto Final – Mercadinho em Python  
Arquivo: `mercadinho.py`

Este é o projeto principal do repositório e representa a aplicação prática de todos os conceitos estudados nos exercícios anteriores. Diferente dos outros arquivos, que trabalham conteúdos de forma isolada, o Mercadinho une tudo em um único sistema funcional, simulando um pequeno mercado no terminal.

A escolha desse projeto foi proposital: ele aproxima o estudo da programação de uma situação real, onde é necessário cadastrar dados, exibir informações, validar opções do usuário e realizar cálculos automaticamente.

O sistema funciona por meio de um menu interativo que permanece ativo até o usuário decidir sair.

### Funcionalidades do Mercadinho

- Cadastro de produtos com nome e preço  
- Listagem de todos os produtos cadastrados  
- Simulação de compra de múltiplos produtos  
- Cálculo automático do valor total da compra  
- Validação de opções inválidas  
- Finalização segura da compra  

### Como funciona internamente

Os produtos são armazenados em uma lista, onde cada produto é representado por um dicionário contendo duas informações: nome e preço. Esse formato permite organizar os dados de forma simples e eficiente:

```python
[
  {"nome": "Arroz", "preco": 25.0},
  {"nome": "Feijão", "preco": 9.5}
]
````

Durante a compra, o sistema exibe todos os produtos disponíveis e o usuário seleciona os itens pelo número correspondente. Cada escolha adiciona automaticamente o valor ao total da compra. Ao digitar 0, a compra é encerrada e o valor final é exibido.

### Como executar o Mercadinho

```bash
python mercadinho.py
```

Ao executar, o sistema exibe automaticamente o menu:

```
=== MERCADINHO DO JUSTKE 💸 ===
1 - Cadastrar produto
2 - Listar produtos
3 - Comprar produtos
4 - Sair
```

### Objetivo do Mercadinho dentro do projeto

O Mercadinho tem como objetivo consolidar o aprendizado, mostrando como listas, dicionários, condicionais, laços de repetição, entrada de dados e cálculos funcionam juntos dentro de um único sistema. Ele marca a transição dos exercícios básicos para a construção de um programa completo e funcional.

```

## 🎯 Objetivo do Repositório

Este repositório tem como objetivo fortalecer a base da programação em Python, passando por cada conceito separadamente e depois aplicando tudo em um projeto completo.

Ele representa a transição do aprendizado teórico para a prática real, com sistemas funcionando de verdade.
