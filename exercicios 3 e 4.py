"""
3 Faça um Programa que peça dois numeros e imprima a soma.
4 Faça um Programa que peça as 4 notas bimestrais e mostre a média
"""

# Pede os números ao utilizador
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
# Calcula e imprime a soma
soma = int(num1 + num2)
print(f"A soma dos dois números é: {soma}")

print("------------")
# 4 notas bimestrais e mostre a média
nota1 = int(input("Digite a nota do 1º bimestre: "))
nota2 = int(input("Digite a nota do 2º bimestre: "))
nota3 = int(input("Digite a nota do 3º bimestre: "))
nota4 = int(input("Digite a nota do 4º bimestre: "))

soma = nota1 + nota2 + nota3 + nota4
media = soma / 4
# a media é:_____
print(f"a media é:", media)

print("------------")