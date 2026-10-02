"""Cadastro simples de usuários usando arquivo texto."""

ARQUIVO_USUARIOS = "usuarios.txt"


def cadastrar_usuario():
    nome = input("Digite o nome: ").strip()
    idade = input("Digite a idade: ").strip()
    email = input("Digite o e-mail: ").strip()

    with open(ARQUIVO_USUARIOS, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome} - {idade} anos - {email}\n")

    print(f"{nome} cadastrado com sucesso!\n")


def listar_usuarios():
    print("\n=== Lista de Usuários ===")

    try:
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as arquivo:
            usuarios = [linha.strip() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        usuarios = []

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        print(usuario)


def menu():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()
