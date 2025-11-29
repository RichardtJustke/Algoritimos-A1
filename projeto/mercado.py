produtos = []

def mostrar_menu():
    print("\n=== MERCADINHO DO JUSTKE 💸 ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produtos")
    print("4 - Sair")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço do produto: R$ "))

        produto = {
            "nome": nome,
            "preco": preco
        }

        produtos.append(produto)
        print("✅ Produto cadastrado com sucesso!")

    elif opcao == "2":
        print("\n📦 PRODUTOS DISPONÍVEIS:")
        
        if len(produtos) == 0:
            print("Nenhum produto cadastrado ainda.")
        else:
            for i, item in enumerate(produtos):
                print(f"{i + 1} - {item['nome']} - R$ {item['preco']:.2f}")

    elif opcao == "3":
        if len(produtos) == 0:
            print("⚠️ Não tem produtos para comprar!")
        else:
            total = 0
            print("\n🛒 HORA DAS COMPRAS:")

            for i, item in enumerate(produtos):
                print(f"{i + 1} - {item['nome']} - R$ {item['preco']:.2f}")

            while True:
                escolha = input("Digite o numero do produto (ou 0 para finalizar): ")

                if escolha == "0":
                    break

                indice = int(escolha) - 1

                if indice >= 0 and indice < len(produtos):
                    total += produtos[indice]["preco"]
                    print("Produto adicionado ao carrinho ✅")
                else:
                    print("Produto inválido ❌")

            print(f"\n💰 Total da compra: R$ {total:.2f}")

    elif opcao == "4":
        print("Saindo do mercado... Valeu demais! 👋")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
