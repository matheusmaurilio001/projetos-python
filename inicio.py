idade = (input("qual a sua idade?"))
if idade <= 11:
    print ("criança")
elif idade <= 17:
    print("adolescente")
elif idade <= 59:
    print("adulto")
elif idade >= 60:
    print ("idoso")
else:
    print("SOMENTE NUMEROS, repita o processo")