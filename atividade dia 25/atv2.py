def catalogo_alunos():
    alunos = {}

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        try:
            nota = float(input(f"Digite a nota de {nome}: "))
            alunos[nome] = nota
        except ValueError:
            print("Por favor, insira um número válido para a nota.")

    if alunos:
        media = sum(alunos.values()) / len(alunos)
        print(f"\nMédia da turma: {media:.2f}")
        print("Alunos com notas acima da média:")
        for aluno, nota in alunos.items():
            if nota > media:
                print(f"{aluno} - Nota: {nota:.2f}")
    else:
        print("Nenhum aluno cadastrado.")

# Execução do programa
if __name__ == "__main__":
    catalogo_alunos()
