def consultar_preco():
    precos_produtos = {
        "Iphone": 35000,
        "Banana": 2.00,
        "Laranja": 4.00,
        "Pão": 1.50
    }
    produto = input("Digite o nome do produto que deseja consultar: ")
    
    if produto in precos_produtos:
        print(f"O preço de {produto} é R$ {precos_produtos[produto]:.2f}")
    else:
        print("Produto não encontrado.")

# Chamando a função
consultar_preco()