temperaturas = []
print("informe 7 temperaturas: ")

media = 33.5
igual_ou_acima = 0
abaixo = 0 

for i in range(7):
    temp = int(input(f"Informe a {i+1} temperatura: "))
    if temp < media:
        abaixo = abaixo + 1
        
    elif temp >= media:
        
        igual_ou_acima = igual_ou_acima + 1
    
print(f"Temperaturas iguais ou acima da média: {igual_ou_acima}")
print(f"Temperaturas abaixo da média: {abaixo}")