"""
for repete um número determinado numero de vezes
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
