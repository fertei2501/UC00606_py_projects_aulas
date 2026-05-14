"""
1 - faça um programa em python que peça numeros ao utilizador ate ser inserido um numero negativo
1.2 - conte os números impar inseridos
1.3 - mostre apenas os números pares
1.4 - calcule a media dos números ímpar
1.5 - indique o maior e o menor (sem usar listas)
"""
print("--"*10)
contador = 0
soma = 0
maior = -1
menor = -1
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break

    if maior == -1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    if n % 2 == 0:
        print(n)
    else:
        soma += n
        contador += 1
media = soma / contador
print(f"A média dos números ímpares é:", media)
print("--"*10)
