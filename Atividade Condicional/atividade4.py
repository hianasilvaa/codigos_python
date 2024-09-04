altura = float(input("Digite a altura da pessoa em metros: "))
sexo = input("Digite o sexo da pessoa (M para masculino ou F para feminino): ")

if sexo == "M":
    peso = (72.7 * altura) - 58
    print(f"peso ideal: {peso:.2f}kg")

elif sexo == "F":
    peso = (62.1 * altura) - 44.7
    print(f"peso ideal: {peso:.2f}kg")

else:
    print(f"tente novamente ")
