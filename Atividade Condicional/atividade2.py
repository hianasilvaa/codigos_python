salario = float(input("informe o seu salário: R$"))

if salario < 600:
    aumento = salario * 0.30
    novo_salario = salario + aumento
    print(f"seu novo salário é R${novo_salario:.2f}.")

else:
    print(f"Você não tem direito ao aumento.")