alunos = []

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para finalizar): ")

    if nome.lower() == "sair":
        break

    alunos.append(nome)

print("\nLista de alunos cadastrados:")
for aluno in alunos:
    print(aluno)
