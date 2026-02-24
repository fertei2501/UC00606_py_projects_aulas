"""
5 Faça um Programa que converta metros para centímetros.
6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
# Pede o valor em metros
metros = float(input("Digite o valor em metros: "))

# Converte para centímetros (1m = 100cm)
centimetros = metros * 100

# Exibe o resultado
print(f"{metros} metros equivalem a {centimetros:.0f} centímetros.")

print("------------")
import math

# Pede o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcula a área usando a fórmula (pi * raio ao quadrado)
area = math.pi * (raio ** 2)

# Exibe o resultado com duas casas decimais
print(f"A área do círculo com raio {raio} é: {area:.2f}")

print("------------")
