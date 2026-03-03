"""
5 Faça um Programa que converta metros para centímetros.
6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
# Pede o valor em metros
valor = float(input("valor em metros: "))

# Converte para centímetros (1m = 100cm)
cm = valor * 100

# Exibe o resultado
print(f"{valor:.2f}m equivalem a {cm:.2f}cm")

print("------------")
import math

# Pede o raio do círculo
raio_circulo = float(input("raio do círculo: "))

# Calcula a área usando a fórmula (pi * raio ao quadrado)
area = math.pi * raio_circulo ** 2

# Exibe o resultado com duas casas decimais
print(f"A área do círculo com raio {raio_circulo} é: {area:.3f}")

print("------------")
