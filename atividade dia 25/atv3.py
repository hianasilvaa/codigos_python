def comparar_idades(idade1, idade2):
    if idade1 > idade2:
        return "A primeira pessoa é mais velha."
    elif idade2 > idade1:
        return "A segunda pessoa é mais velha."
    else:
        return "As duas pessoas têm a mesma idade."

def main():
    while True:
        idade1 = int(input("Digite a idade da primeira pessoa (ou 0 para sair): "))
        if idade1 == 0:
            break
        idade2 = int(input("Digite a idade da segunda pessoa: "))
        
        resultado = comparar_idades(idade1, idade2)
        print(resultado)

# Execução do programa
if __name__ == "__main__":
    main()
