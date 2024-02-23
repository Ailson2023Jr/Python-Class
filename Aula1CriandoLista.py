# Criando uma lista de números
numeros = [1,2,3,4,5]

#Imprimindo a lista
print ("Lista de  números:", numeros)

# Acessando o primeiro elemento epecífico pelo índice
print("Primeiro elemento:", numeros[0])
print("Segundo elemento:", numeros[1])

# Adicionando um novo elemento especifico da lista
numeros.append (6)

# Removendo um elemento especifico da lista
numeros.remove (3)

# Verificando o tamanho da lista
tamanho = len(numeros)
print("Tamanho da lista:", tamanho)

# Verificando se um elemento está na lista
if 4 in numeros:
    print ("O número 4 está na lista.")
else:
    print("O número 4 não está na lista.")

 # Percorrendo a lista com um Loop for
print ("Elementos da lista:")    
for numero in  numeros:
    print (numero)

