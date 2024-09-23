def add_temperatura():
    temperaturas = {}
    
    for i in range(5):
        cidade = input(f"Digite o nome da cidade {i + 1}: ")
        temperatura = float(input(f"Digite a temperatura em {cidade}: "))
        temperaturas[cidade] = temperatura
    
    print("Dicionário de temperaturas:")
    print(temperaturas)

# Chamando a função
add_temperatura()
