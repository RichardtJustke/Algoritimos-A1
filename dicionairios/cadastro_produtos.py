produtos = {}

while True:
    nome = input("Digite o nome do produto (ou 'sair' para finalizar): ")

    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço do produto: R$ "))
    produtos[nome] = preco

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():
    print(f"{nome} - R$ {preco:.2f}")
