# faça um programa que peça ao utilizador números,
# quando for introduzido um valor negativo deixa de pedir números

while True:
    n = int(input("Introduza um número: "))
    print(f"o número introduzido foi {n}")
    if n < 0:
        print(f"valor negativo, vai terminar...")
        break # o loop termina
print("-----------")

# faça um programa que peça até 100 números ao utilizador,
# quando for introduzido um valor negativo deixa de pedir números

print("Introduza até 100 números:")

for i in range(100):
    num = int(input(f"{i + 1}º Número: "))
    if num < 0:
        print(f"valor negativo, loop terminado")
        break
print("-----------")