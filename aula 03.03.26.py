#Faça um Programa que peça um valor e mostre na consola se o valor é positivo ou negativo.

num = 2
if num > 0:
    print(f"{num} é um número positivo")
else:
    print(f"{num} é um número negativo")

print("------------")
# Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever:
#   F - Feminino,
#   M - Masculino,
#   Sexo Inválido

genero = "M"
if genero == "M":
    print(f"{genero} é Masculino")
elif genero == "F":
    print(f"{genero} é Feminino")
else:
    print(f"{genero} é sexo Inválido")

#fim codigo
print("-----------")

# Faça um programa que verifique se uma letra digitada é vogal ou consoante

letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print(f"{letra} é uma vogal.")
elif letra in "1234567890":
    print(f"{letra} é uma entrada inválida. Por favor, digite uma letra.")
else:
    print(f"{letra} é uma consoante.")
print("-----------")
# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada pelo aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a 10;
# A mensagem "Reprovado", se a média alcançada for menor do que 10;
# A mensagem "Aprovado com Distinção" se a média for igual a 20.

nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
media = (nota1 + nota2) / 2
print(f"a media foi {media:.2f}")
if media == 20:
    print(f"Aprovado com Distinção")
elif media >= 10:
    print(f"Aprovado")
else:
    print(f"Reprovado")

#fim codigo
print("-----------")