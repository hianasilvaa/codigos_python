impares = 0 

while True:
    valor = int(input("digite um valor númerico (ou 0 para parar): "))
    if valor == 0:
        break #sair de um loop 
    if valor % 2 != 0:
        impares += 1
        
print(f"quantidade de valores ímpares: {impares}")