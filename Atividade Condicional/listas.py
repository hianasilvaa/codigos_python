animais = ['cachorro','Gato','Ovelha']
print(type(animais)) #exibindo o tipo da variável

print(animais)

print('-'*50)
#Estamos exibindo todos os itens da lista 'animais'
for elementos in animais:
    print(elementos)
    
#1ª etapa: Atualização de dados
print('-'*50)
animais[0] = 'Coelho'
print(animais)

#2ª etapa: Inserir itens na lista 
print('-'*50)
#forma 1 - usando appeend
animais.append("Cavalo")# irá inserir um novo item no final da lista
print(animais)

#forma 2 - usando insert
animais.insert(1,"Pássaro")# o insert precisa de 2 valores, o 1º será o índice da lista que desejo inserir o valor. o 2º é o conteúdo que quero inserir na lista
print(animais)

#3ª etapa: Excluir itens na lista
print('-'*50)

#forma 1 - usando pop()
animais.pop()# irá excluir sempre o último item
print(animais)

#forma 2 - usando pop() com índice
animais.pop(0)# Aqui íremos escolher qual índice da lista será excluído.
print(animais)

#forma 3 - usando remove
animais.remove("ovelha") # irá remover o item pelo seu conteúdo
print(animais)