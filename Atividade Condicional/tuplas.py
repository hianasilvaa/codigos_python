# Trabalhando com tuplas

objetos = ('Lápis','Borrachas','caderno')

print(type(objetos))# a função type() irá exibir o tipo da variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1]) # estamos exibindo apenas um item, que está na posição 1

# Exibido todos os dados da tupla
print('_'*50)

for item in range(0,3):
    print(objetos[item])
    
#Exibindo todos ps dados sem a função range 
print('-'*50)

for item in objetos:
    print(item)
    
    objetos[0] = 'Caneta' #ocorre um erro pois os valores de uma tupla
    print(objetos)