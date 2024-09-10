idade = int(input("informe a sua idade: "))

if idade <12:
    print("você é uma criança.")
elif idade > 12 and idade <18:
    print("você é um adolescente.")
elif idade > 18 and idade < 60:
    print("você é um adulto.")
elif idade > 60:
    print("voê é um(a) idoso")      