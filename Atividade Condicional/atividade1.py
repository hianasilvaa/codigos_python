valor = int(input("informe um valor numérico:"))

if valor >= 200:
    print(f"o número {valor} é maior ou igual a 200")
# elif é o mesmo que else if, junção dos dois 
elif valor >= 100 and valor < 200: 
    print(f"o número {valor} está entre 100 e 200\n")
else:
    print(f"o número {valor} é menor que 100 e 200\n")