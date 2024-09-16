soma_positivos = 0
contador = 0
quantidade_negativos = 0
    
print("Digite 10 valores inteiros:")
    
for i in range(10):
        valor = int(input(f"Digite o valor {contador+1}: "))
        
        if valor > 0:
            soma_positivos += valor
        elif valor < 0:
            quantidade_negativos += 1
    
print(f"\nA soma dos números positivos é: {soma_positivos}")
print(f"A quantidade de valores negativos é: {quantidade_negativos}")
    