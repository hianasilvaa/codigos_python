lista1 = []
lista2 = []
resultado = []

print("Digite 9 valores para a primeira lista:")
for i in range(9):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista1.append(valor)

print("Digite 9 valores para a segunda lista:")
for i in range(9):
    valor = int(input(f"Digite o {i+1}º valor: "))
    lista2.append(valor)

# Soma os valores das duas listas e armazena na terceira lista
for i in range(len(lista1)):
    resultado.append(lista1[i] + lista2[i])
print("Resultado da soma das duas listas:", resultado)
