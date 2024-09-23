pessoa = ["Maria", "48", "Rua 10"]
print(pessoa)

# Iniciando com dicionário
dados_pessoais = {
    'Nome': 'João',
    'Idade': 18,
    'Endereço': 'Avenida 4'
    }

print(dados_pessoais)

#Exibindo as chaves ultilizando o comando keys()
print(dados_pessoais.keys())

#Exibindo os valores utilizando o comando values()
print(dados_pessoais.values())

#Exibindo tanto a chave quanto o valor com o comando itens()
print(dados_pessoais.itens())

#Exibindo o dicionário detalhado

for chave, valor in dados_pessoais.itens():
    print(f"{chave} : {valor}")
    
#Realizando operação com dicionário
#Adicionando dados ao dicionário
#orma 1
dados_pessoais["peso"] = 68
print(dados_pessoais)

#Forma 2 - usando o comando update()
dados_pessoais.update({"Profissão":"Engenheio"})
print(dados_pessoais)

#renomer dados usando dicionário
#Forma 1 - usando pop()
dados_pessoais.pop("idade")#Preciso passar a chave para poder excluir o registro
print(dados_pessoais)

#Forma 2 - usando del()
del(dados_pessoais)["Endereço"]
print(dados_pessoais)