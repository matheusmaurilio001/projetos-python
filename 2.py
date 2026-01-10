#Cadastro de Usuários
#Salva nome, idade e email em arquivo usuarios.txt
 
def cadastrar_usuario():
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    email = input("Digite o email: ")
    
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome} - {idade} anos - {email}\n")
    
    print(f"{nome} cadastrado com sucesso!\n")
 
def listar_usuarios():
    print("\n=== Lista de Usuários ===")
    try:
        with open("usuarios.txt", "r") as arquivo:
            conteudo = arquivo.readlines()
            if len(conteudo) == 0:
                print("Nenhum usuário cadastrado.")
            else:
                for linha in conteudo:
                    print(linha.strip())
    except FileNotFoundError:
        print("Nenhum usuário cadastrado ainda.")
 
def menu():
    while True:
        print("\n1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")
 
menu()
 