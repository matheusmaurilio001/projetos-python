operaçoes = int(input("qual operaçao deseja escolher? opçoes: 1 adiçao, 2 multiplicaçao, 3 divisao:"))
match operaçoes: 
    case 1:
        numero1 = int(input("escolha um numero:"))
        numero2 = int(input("escolha um numero:"))
        print(numero1 + numero2)
    case 2:
        numero1 = int(input("escolha um numero:"))
        numero2 = int(input("escolha um numero:"))
        print(numero1  * numero2)
    case 3:
        numero1 = int(input("escolha um numero:"))
        numero2 = int(input("escolha um numero:"))
        print(numero1 / numero2)
    case _:
        print("apenas numeros, repita")
