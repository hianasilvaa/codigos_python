contador = 0
for cont in range (5):
    idade = int(input("Digite as idades: "))
    
    if idade >= 18:
        contador +=1
print(f"quantidade de pessoa com 18 anos ou mais:{contador}")