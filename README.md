<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <title>Projetos em Python – Fundamentos da Programação</title>
</head>
<body>
  <h1>🐍 Projetos em Python – Fundamentos da Programação</h1>

  <p>
    Este repositório reúne as atividades práticas desenvolvidas durante o estudo de lógica de programação em Python,
    juntamente com um projeto final que une todos os conceitos em um único sistema funcional: o Mercadinho.
  </p>
  <p>
    As atividades foram criadas para praticar os fundamentos da programação separadamente, e o projeto final foi desenvolvido
    para aplicar tudo em um contexto real, simulando um sistema de mercado no terminal.
  </p>

  <hr />

  <h2>🎯 Objetivo das Atividades</h2>
  <p>
    O principal objetivo dessas práticas foi transformar a teoria em algo prático, entendendo como:
  </p>
  <ul>
    <li>As decisões são tomadas dentro de um sistema</li>
    <li>Os dados são armazenados e organizados</li>
    <li>As repetições automatizam tarefas</li>
    <li>O usuário interage com o programa</li>
    <li>Os cálculos acontecem de forma automática</li>
  </ul>
  <p>
    Cada atividade trabalha um conceito específico, e ao final todos eles são utilizados juntos no projeto do Mercadinho.
  </p>

  <hr />

  <h2>📁 Estrutura do Repositório</h2>

  <pre><code>A1-Algoritmos/
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
  </code></pre>

  <hr />

  <h2>✅ Práticas Desenvolvidas</h2>

  <h3>1️⃣ Estruturas Condicionais – Verificação de Idade</h3>
  <p>
    Nesta prática foi desenvolvido um programa que solicita a idade do usuário e decide se ele pode entrar em um evento ou não.
  </p>
  <p>Com isso, foi praticado:</p>
  <ul>
    <li>Tomada de decisão</li>
    <li>Uso de <code>if</code>, <code>elif</code> e <code>else</code></li>
    <li>Entrada de dados pelo usuário</li>
  </ul>

  <h3>2️⃣ Estruturas de Repetição – Números Pares</h3>
  <p>
    Nesta atividade o sistema exibe os números pares de 1 até 100 utilizando <code>for</code> e <code>while</code>.
  </p>
  <p>Aqui foi possível aprender:</p>
  <ul>
    <li>Repetição automática de tarefas</li>
    <li>Controle de laços</li>
    <li>Uso de operadores matemáticos</li>
  </ul>

  <h3>3️⃣ Listas – Cadastro de Alunos</h3>
  <p>
    Foi criado um programa que permite cadastrar vários nomes de alunos e exibi-los no final.
  </p>
  <p>Nesta prática foi trabalhado:</p>
  <ul>
    <li>Armazenamento de vários dados em uma lista</li>
    <li>Entrada contínua de dados</li>
    <li>Laços de repetição para controle do cadastro</li>
  </ul>

  <h3>4️⃣ Dicionários – Cadastro de Produtos</h3>
  <p>
    Nesta atividade foi criado um sistema simples de cadastro de produtos utilizando dicionário.
  </p>
  <p>Aqui foi aprendido:</p>
  <ul>
    <li>Organização de dados em chave e valor</li>
    <li>Armazenamento de nome e preço</li>
    <li>Exibição estruturada das informações</li>
  </ul>

  <hr />

  <h2>🛒 Projeto Final – Sistema de Mercadinho em Python</h2>
  <p><strong>Arquivo:</strong> <code>mercadinho.py</code></p>

  <p>
    Este sistema foi criado pensando em pequenos mercadinhos, lojinhas de bairro ou negócios simples que não possuem um sistema
    de cadastro e controle de compras. Em muitos desses lugares, tudo ainda é feito no papel, o que pode causar erros de soma,
    confusão nos valores e falta de organização.
  </p>
  <p>
    O sistema resolve esse problema funcionando como um <strong>caixa simples no computador</strong>, onde é possível cadastrar
    produtos, listar os itens disponíveis e realizar compras com cálculo automático do valor total.
  </p>

  <h3>👤 Para quem esse sistema resolve o problema</h3>
  <ul>
    <li>Pequenos comerciantes</li>
    <li>Lojinhas de bairro</li>
    <li>Estudantes que querem entender como funciona um sistema real</li>
    <li>Qualquer pessoa que queira simular um caixa simples</li>
  </ul>

  <h3>🔄 Como o sistema funciona na prática</h3>
  <ol>
    <li>O operador cadastra os produtos com nome e preço</li>
    <li>Os produtos ficam armazenados no sistema</li>
    <li>Quando um cliente vai comprar, o operador escolhe os produtos pelo número</li>
    <li>Cada item selecionado é somado automaticamente</li>
    <li>Ao finalizar, o sistema mostra o total da compra</li>
    <li>O operador pode iniciar outra compra ou encerrar o sistema</li>
  </ol>

  <h3>🧱 Organização dos Dados no Sistema</h3>
  <p>
    Os produtos são armazenados em uma lista, onde cada produto é um dicionário com nome e preço:
  </p>

  <pre><code>[
  {"nome": "Arroz", "preco": 25.0},
  {"nome": "Feijão", "preco": 9.5}
]
  </code></pre>

  <h3>▶️ Como Executar o Sistema</h3>
  <pre><code>python mercadinho.py
  </code></pre>

  <p>Ao iniciar, o sistema exibe o menu:</p>

  <pre><code>=== MERCADINHO DO JUSTKE 💸 ===
1 - Cadastrar produto
2 - Listar produtos
3 - Comprar produtos
4 - Sair
  </code></pre>

  <hr />

  <h2>🧠 O Que Foi Aprendido com o Projeto</h2>
  <p>
    Com este repositório foi possível aprender, na prática:
  </p>
  <ul>
    <li>Como funciona um sistema real por dentro</li>
    <li>Como os dados são cadastrados e armazenados</li>
    <li>Como o usuário interage com o sistema</li>
    <li>Como validar opções inválidas</li>
    <li>Como realizar cálculos automaticamente</li>
    <li>Como organizar um projeto em pastas</li>
    <li>Como documentar um projeto com README</li>
    <li>Como subir um projeto no GitHub</li>
  </ul>

  <hr />

  <h2>🧩 Pseudocódigo do Sistema do Mercadinho</h2>

  <pre><code>iniciar lista de produtos vazia

enquanto o sistema estiver ativo:
    mostrar menu

    se opção for cadastrar:
        pedir nome
        pedir preço
        salvar produto na lista

    se opção for listar:
        se não houver produtos:
            mostrar aviso
        senão:
            mostrar todos os produtos

    se opção for comprar:
        se não houver produtos:
            mostrar aviso
        senão:
            iniciar total da compra
            mostrar produtos
            enquanto não finalizar:
                pedir número do produto
                se número for válido:
                    somar preço ao total
                senão:
                    avisar erro
            mostrar total final

    se opção for sair:
        encerrar sistema
  </code></pre>

  <hr />

  <h2>🛠️ Tecnologias Utilizadas</h2>
  <ul>
    <li>Python 3</li>
    <li>Terminal</li>
    <li>Git</li>
    <li>GitHub</li>
  </ul>

  <hr />

  <h2>✅ Conclusão</h2>
  <p>
    Este repositório representa a evolução do aprendizado da lógica de programação, saindo de exercícios isolados até a
    construção de um sistema completo que resolve um problema real. Ele demonstra, na prática, como os conceitos básicos da
    programação se conectam para formar um sistema funcional.
  </p>
</body>
</html>
