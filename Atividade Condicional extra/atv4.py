salario = float(input("Digite o salario: R$ "))

if salario <= 1900:
    print( "você está isento.")
    
elif 1901 <= salario <= 2800:
    imposto = salario * 0.075
    print(f"seu imposto de renda é: {imposto}")
    
elif salario == 2801 >= 3700:
    imposto = salario * 0.15
    print(f"Seu imposto de resnda é {imposto}")
elif salario > 3700:
    imposto =  salario * 0.225
    print(f"Seu imposto de renda é: R$ {imposto:.2f}")
    