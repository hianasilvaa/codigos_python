somar_pesos = 0
somar_idades = 0

for contador in range(5):
    peso = float(input(f"informe seu peso {contador+1}: "))
    idade = float(input(f"informe sua idade {contador+1}: "))
    
    somar_pesos = somar_pesos + peso
    somar_idades = somar_idades + idade
    
print(f"A média de peso do time é {somar_pesos/5}")
print (f"A média da idade do time é {somar_idades/5}")