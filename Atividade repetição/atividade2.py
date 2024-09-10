total_peso = 0
total_idade= 0
num_jogadores = 5
 
for contador in range(num_jogadores):
     print(f"Digite os dados do jogador {contador + 1}:")
     peso= float(input("Digite o peso da pessoa em kg: "))
     idade= (input("Digite a idade em anos: "))

    # Calcula as médias   
     media_peso = total_peso / num_jogadores
     media_idade = total_idade / num_jogadores
     
     print(f"peso ideal: {peso:.2f}anos")
     print(f"Idade média do time: {media_idade:.2f} kg")