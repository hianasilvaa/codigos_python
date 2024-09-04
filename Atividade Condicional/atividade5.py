#leitura dos dados 
distancia = float(input("Digite o percurso em quilômetros: "))
tipo_carro = int(input("Digite o tipo de carro (1, 2 ou 3): "))

# Definição do consumo por tipo de carro
if tipo_carro == 1:
    consumo_por_km = 8
elif tipo_carro == 2:
    consumo_por_km = 9
elif tipo_carro == 3:
    consumo_por_km = 12

# Cálculo do consumo estimado
if consumo_por_km:
    consumo_estimado = distancia / consumo_por_km
    print(f"O consumo estimado de combustível é de {consumo_estimado:.2f} litros.")