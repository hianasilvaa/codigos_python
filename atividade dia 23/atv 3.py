def calcular_bonus(salario, anos_servico):
    if anos_servico <= 5:
        bonus = salario * 0.05
    elif 6 <= anos_servico <= 10:
        bonus = salario * 0.10
    else:
        bonus = salario * 0.15
    return bonus

def main():
    salario = float(input("Informe o salário atual: R$ "))
    anos_servico = int(input("Informe o número de anos de serviço: "))

    bonus = calcular_bonus(salario, anos_servico)
    salario_final = salario + bonus
    print(f"\nBônus: R$ {bonus:.2f}")
    print(f"Salário final com bônus: R$ {salario_final:.2f}")

main()
