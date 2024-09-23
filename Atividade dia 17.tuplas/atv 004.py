temperaturas = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
sm_temperaturas = 0
contador = 0

# Solicita a temperatura média de cada mês
for temps in range(12):
    temp = int(input(f"Informe a temperatura média de {meses[temps]}: "))
    temperaturas.append(temp)


for temperatura in temperaturas:
    sm_temperaturas += temperatura
    contador += 1

media = sm_temperaturas / contador

print(f"Média anual das temperaturas: {media:.2f}°C")

# Exibe as temperaturas acima da média anual com os meses correspondentes
print("Temperaturas acima da média anual:")
for num_mes in range(12):
    if temperaturas[num_mes] > media:
        print(f"{meses[num_mes]}: {temperaturas[num_mes]:.2f}°C")