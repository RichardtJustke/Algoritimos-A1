idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Entrada proibida.")
elif idade < 18:
    print("Entrada permitida apenas com autorização.")
else:
    print("Entrada totalmente liberada.")
