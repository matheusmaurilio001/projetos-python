"""Calculadora simples para prática de estruturas condicionais em Python."""

def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Digite apenas números.")


def main():
    print("=== Calculadora ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    opcao = input("Escolha uma opção: ")

    if opcao not in {"1", "2", "3", "4"}:
        print("Opção inválida.")
        return

    numero1 = ler_numero("Primeiro número: ")
    numero2 = ler_numero("Segundo número: ")

    if opcao == "1":
        resultado = numero1 + numero2
    elif opcao == "2":
        resultado = numero1 - numero2
    elif opcao == "3":
        resultado = numero1 * numero2
    else:
        if numero2 == 0:
            print("Não é possível dividir por zero.")
            return
        resultado = numero1 / numero2

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
