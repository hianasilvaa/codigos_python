def catalogo_livros():
    catalogo = {}
    while True:
        print("\nCatálogo de Livros")
        print("1. Adicionar livro")
        print("2. Remover livro")
        print("3. Exibir catálogo")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            catalogo[titulo] = autor
            print(f"Livre '{titulo}' adicionado.")
        elif opcao == '2':
            titulo = input("Digite o título do livro a ser removido: ")
            if titulo in catalogo:
                catalogo[titulo]
                print(f"Livre '{titulo}' removido.")
            else:
                print("Livro não encontrado.")
        elif opcao == '3':
            print("\nCatálogo Completo:")
            for titulo, autor in catalogo.items():
                print(f"Título: {titulo}, Autor: {autor}")
            print(f"Total de livros: {len(catalogo)}")
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")