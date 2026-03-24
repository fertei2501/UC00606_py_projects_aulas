"""
for repete valores um determinado número de vezes (sabemos quantas vezes repetir)
while repete valores um indeterminado números de vezes (não sabemos quantas vezes repetir,
ou queremos repetir indefinidamente)
"""
"""
## range (gera um intervalo de numeros sequenciais)
range(5) # 0, 1, 2, 3, 4 -> range(n) -> todos os num int 0 e n-1
range(3) # 0, 1, 2

range(2, 5)  # 2, 3, 4 -> range(m, n) -> todos os num int m e n-1
range(10, 20, 2) # 10, 12, 14, 16, 18 -> -> range(m, n, s) -> todos os num int m e n-1 com
# um step de s
# range(lb, ub, s) --> lb ate ub-1 com step s
# num int de 0 a 100 de 5 em 5
range(0, 20, 5)  # 0 ate 20-1 mas de 5 em 5 
# 0, 5, 10, 15
"""

#crie um intervalo com todos os num de 20 a 45 com um step de 3
x = range(20, 45, 3)
for n in x:
  print(n)
print("-----------")

# que num estão nos range
# range(3, 8, 2)
print(list(range(3, 8, 2))) # 3, 5, 7
print("-----------")
# range(3, 10, 3)
print(list(range(3, 10, 3))) # 3, 6, 9
print("-----------")
# range(7, 10, 3)
print(list(range(7, 10, 3))) # 7
print("-----------")

for i in range(5):
  print(i)

print("-----------")
for num in range(3, 8, 2):
  print(num)

print("-----------")
#faça um programa que calcule a tabuada do 2, deve usar um for:
tabuada = int(input("tabuada: "))
for i in range(10):
    aux = i + 1
    print(f"{tabuada} x {aux:2} = {aux * tabuada:2}")

print("-----------")
print(f"Tabuada do numero 2:")
for num in range(1, 11):
    resultado = 2 * num
    print(f"2 x {num} = {resultado}")

print("-----------")
# calcule o fatorial de n, o valor n deve ser pedido ao utilizador; deve usar um for
n = 3
fatorial = 1
for i in range(1, n + 1):
    fatorial *= i
print(f"O fatorial de {n} é {fatorial}")

print("-----------")
n = 4
fatorial = 1
for i in range(n, 1, -1):
    fatorial *= i
print(f"{n}! = {fatorial}")

print("-----------")