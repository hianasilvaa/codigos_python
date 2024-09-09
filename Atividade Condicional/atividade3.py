salario = float(input("informe o seu salário: R$"))
financiamento = float(input("informe o valor do financiamento: R$"))

conversao = salario*5

if financiamento < conversao:
    print("financiamento concedido.")
else:
    print("financiamento negado.")
    
print('obrigado por nos consultar')
    