import random

resultados = ["Cara", "Coroa"]

historico = []

while True:
    # Simular o lançamento da moeda
    resultado = random.choice(resultados)
    print(f"\nO resultado é: {resultado}")
    historico.append(resultado)


    while True:
        resposta = input("Você quer lançar a moeda novamente? (sim/não): ")
        
        if resposta == "sim" or resposta == "s":
            break
        elif resposta == "não" or resposta == "n":
            exit_flag = True
            break
        else:
            print("Por favor, responda com 'sim' ou 'não'.")

    if exit_flag:
        break

print("\nTodos os resultados:")
for resultado in historico:
    print(resultado)