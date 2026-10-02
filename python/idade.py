"""Classifica uma pessoa por faixa etária."""

def main():
    try:
        idade = int(input("Qual é a sua idade? "))
    except ValueError:
        print("Digite apenas números inteiros.")
        return

    if idade < 0:
        print("A idade não pode ser negativa.")
    elif idade <= 11:
        print("Criança")
    elif idade <= 17:
        print("Adolescente")
    elif idade <= 59:
        print("Adulto")
    else:
        print("Idoso")


if __name__ == "__main__":
    main()
