num = int(input("informe um ano: "))

if num % 400 == 0 or num % 4 == 0 and num % 100 != 0:
     print("Ano bissexto")
     
else:
    print("Não é bissexto")