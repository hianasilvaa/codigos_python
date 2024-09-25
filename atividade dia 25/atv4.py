def calcular_desconto(valor, percentual):
    desconto = valor * (percentual / 100)
    valor_final = valor - desconto
    return valor_final

def main():
    precos_finais = []

    for _ in range(5):
        try:
            valor = float(input("Digite o valor do produto: "))
            percentual = float(input("Digite o percentual de desconto: "))
            valor_final = calcular_desconto(valor, percentual)
            precos_finais.append(valor_final)
            print(f"Valor final com desconto: {valor_final:.2f}")
        except ValueError:
            print("Por favor, insira um número válido.")

    print("\nLista de valores finais com desconto:")
    for preco in precos_finais:
        print(preco)

# Execução do programa
if __name__ == "__main__":
    main()
