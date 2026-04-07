"""
#imagine que tem a lista

nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]

#como obter
# ["Bruno", "Carlos"]
#os últimos 2 elm
# a lista invertida
#os nomes nas pos par (0 é par)

print(nomes[1:3])
print("-----------")
print(nomes[-2:])
print("-----------")
print(nomes[::-1])
print("-----------")
print(nomes[::2])
print("-----------")
"""

"""
tendo a lista:
numeros = [10, 20, 30, 40, 50, 60, 70, 80]

Mostrar os 3 primeiros números
Mostrar os 3 últimos números
Mostrar os números do índice 2 ao 6
Mostrar a lista invertida
Mostrar os números de 2 em 2
Mostrar os últimos 4 números invertidos

todos os valores pares
a soma de todos os impares
soma os ultimos 2
soma os 1os 2

soma os 3 e 4 com os 2 ultimos

"""
numeros = [10, 20, 30, 40, 50, 60, 70, 80]
print(numeros[:3]) # Mostrar os 3 primeiros números
print("---------------")
print(numeros[-3:]) # Mostrar os 3 últimos números
print("---------------")
print(numeros[2:7]) # Mostrar os números do índice 2 ao 6
print("---------------")
print(numeros[::-1]) # Mostrar a lista invertida
print("---------------")
print(numeros[::2]) # Mostrar os números de 2 em 2
print("---------------")
print(numeros[:-5:-1]) # Mostrar os últimos 4 números invertidos
print("---------------")
print(numeros[0:]) # todos os valores pares
print("---------------")
print # a soma de todos os ímpares
print("---------------")
print(sum(numeros[-2:])) # soma os ultimos 2
print("---------------")
print(sum(numeros[:2])) # soma os 1os 2
print("---------------")
print(numeros[3] + numeros[4] + sum(numeros[-2:])) # soma os 3 e 4 com os 2 ultimos
print("---------------")
