horas_trabalhadas= int(input("Digite a quantidade de horas trabalhada: "))
valor_por_hora = float(input("Digite o valor por hora trabalhada: "))

if horas_trabalhadas > 40:
    valor_por_hora *= 1.5
    print(f"seu novo valor po hora será {valor_por_hora}")

else:
    print(f"Você não tem direito ao aumento.")
