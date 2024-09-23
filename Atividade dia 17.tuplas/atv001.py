valores = []
contador_impares = 0

for i in range(7):
    valor = int(input(f"Digite o {i+1}º valor: "))
    valores.append(valor)

for valor in valores:
    if valor % 2 != 0: 
        contador_impares += 1
        
print(f"A quantidade de números ímpares na lista é: {contador_impares}")
