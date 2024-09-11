num = []
for i in range(8):
    numero = float(input(f"Digite número {i+1}: "))
    num.append(numero)
    
    negativo = 0
    soma_positivo = 0 
    
for numero in num:
    if numero < 0:
        negativo +=1
    elif numero > 0:
         soma_positivo += numero

print(f"Número negativo: {negativo}")
print(f"soma dos números positivos: {soma_positivo}")
    