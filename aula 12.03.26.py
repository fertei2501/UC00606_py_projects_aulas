#aula 12.03.26
#loops

# while

contador = 0

while contador <= 10:
    print(contador)
    contador += 1
#fim codigo
print("-----------")

# faça um programa que mostre a tabuada do 2
tab = 2
contador = 1

print(f"Tabuada do numero 2:")
while contador <= 10:
    print(f"{tab} x {contador} = {tab * contador}")
    contador += 1  # Incrementa o contador para não criar um loop infinito
#fim codigo
print("-----------")

#calcule o fatorial de n, o valor n deve ser pedido ao utilizador

n = int(input("num: ")) # n: 3
fatorial = n # fatorial = 3
aux = n # so para nao destruir o n
# n! = n * n-1 * n-2 * ... * 1
# n! = 1 * 2 * 3 * ... * n-1 * n
# 5! = 5 * 4 * 3 * 2 * 1 = 120

while aux > 1:
    aux -= 1
    print(f"{fatorial} x {aux} = {fatorial * aux}")
    fatorial = fatorial * aux

print(f"{n}! = {fatorial} ")

print("-----------")

contador = 100
while contador > 0:
    print(contador)
    if contador == 80: # o valor do contador for par entra
        break # o while termina
    contador -= 1
print("-----------")

# crie um programa que leia no max 100 num,
# mas se o utilizador inserir um valor negativo, termina o programa

#ler no max 100 num

# se num < 0 -> parar

max_num = 100
curr = 1

while curr <= max_num:
    n = int(input(f"num {curr}: "))
    if n < 0:
        break
    curr += 1

print("-----------")