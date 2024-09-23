def calcular_multa(velocidade_registrada, limite_velocidade):
    if velocidade_registrada <= limite_velocidade:
        return "Sem multa"
    elif 1 <= velocidade_registrada - limite_velocidade <= 10:
        return "Multa: R$ 50,00"
    elif 11 <= velocidade_registrada - limite_velocidade <= 20:
        return "Multa: R$ 100,00"
    else:
        return "Multa: R$ 200,00"

velocidade_registrada = float(input("Informe a velocidade registrada do veículo (km/h): "))
limite_velocidade = float(input("Informe o limite de velocidade da via (km/h): "))

resultado = calcular_multa(velocidade_registrada, limite_velocidade)
print(resultado)