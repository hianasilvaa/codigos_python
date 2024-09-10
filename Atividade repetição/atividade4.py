valor_inicial = int(input("informe um valor inicial:"))
valor_final = int(input("informe um valor final:"))

soma = 0

for cont in range(valor_inicial,valor_final):
    soma = soma + cont
    
    print(soma)
