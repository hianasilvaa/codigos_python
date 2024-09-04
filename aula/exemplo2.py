nome = input("informe seu nome: ")
end = input("informe seu endereço: ")
idade = input("informe sua idade: ")

# Exibindo dados das variáveis
#print (nome,end,idade)

#1ª forma de concatenação
print("\nOlá",nome, "seu endereço é",end,"sua idade é",idade)

#2ª forma de concatenação
print("\nOlá {} seu endereço é {} e sua idade é {}".format(nome,end,idade))

#3ª forma de concatenação - f string
print(f"Bem vindo {nome}, você mora na {end} e tem {idade} anos")