valor = int(input("informe um valor numérico:"))

if valor >= 50:
    print(f"o número {valor} é maior ou igual a 50")
# elif é o mesmo que else if, junção dos dois 
elif valor >= 30 and valor < 50: 
    print(f"o número {valor}está entre 30 e 50\n")
else:
    print(f"o número {valor} é menor que 30\n")