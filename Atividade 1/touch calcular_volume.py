# calcular_volume.py

def calcular_volume(comprimento, largura, altura):
    return comprimento * largura * altura

def main():
    # Solicita ao usuário as dimensões da caixa
    comprimento = float(input("Digite o comprimento da caixa (em unidades): "))
    largura = float(input("Digite a largura da caixa (em unidades): "))
    altura = float(input("Digite a altura da caixa (em unidades): "))

    # Calcula o volume
    volume = calcular_volume(comprimento, largura, altura)

    # Exibe o resultado
    print(f"O volume da caixa é: {volume:.2f} unidades cúbicas")

if __name__ == "__main__":
    main()
