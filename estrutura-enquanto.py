#1ª forma de ultilizar while - parecido com o FOR
contador = 1 # inicializando a variável
    
while contador <= 5:
    print(contador)
    contador = contador + 1 # é o mesmo que contador +=1
    
    
print("="*40)

# 2ª forma de ultilizar while - loop condicional normal

valor = 0 # inicializando a variável
while valor >=0:
    valor = int(input("informe um valor qualquer digite um valor negativo para terminar): "))
    
    print(f"você digitou {valor}")

print("="*40)

#3ª forma de ultilizar while - como se fosse faça..enquanto 
while True:
    senha = input("informe a senha: ")
    if senha == "123":
        print("Parabéns,senha correta")
        break #forma de encerrar o while
    else:
        print("Senha incorreta, tente denovo")    