import random
escolhas = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

escolha_computador = random.randint(1, 3)
escolha_usuario = int(input("Escolha uma opção (1 - Pedra, 2 - Papel, 3 - Tesoura): "))

if escolha_usuario == escolha_computador:
    print("Empate!")
elif (escolha_usuario == 1 and escolha_computador == 3) or (escolha_usuario == 2 and escolha_computador == 1) or (escolha_usuario == 3 and escolha_computador == 2):
    print(f"Você escolheu {escolhas[escolha_usuario]} e o computador escolheu {escolhas[escolha_computador]}. Você ganhou!")
else:
    print(f"Você escolheu {escolhas[escolha_usuario]} e o computador escolheu {escolhas[escolha_computador]}. O computador ganhou!")
