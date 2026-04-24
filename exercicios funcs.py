"""
1 Crie uma função msg  que mostre a msg ola mundo
2 Crie uma função saudação  que mostre a msg ola [nome], bem vindo
3 crie uma função que permita cirar uma var com a msg ola [nome], bem vindo
    mostre o a msg (fora da função)

4 Cria uma função chamada dobro que receba um número e devolva o seu dobro.
5 Cria uma função chamada media que receba dois números e devolva a média.

6 Cria uma função chamada par_ou_impar que receba um número e devolva:
    "Par" se for par
    "Ímpar" se for ímpar
7 Cria uma função chamada maior que receba dois números e devolva o maior.

8 Cria uma função chamada positivo_negativo que receba um número e devolva:
    "Positivo"
    "Negativo"can
    "Zero"
-- Nova --
9 Cria uma função chamada tabuada que receba um número e imprima a tabuada desse número (de 1 a 10).
"""


#1 Crie uma função msg  que mostre a msg ola mundo
def msg():
    print("ola mundo")
    print("-----------------")
msg()

#2 Crie uma função saudação  que mostre a msg ola [nome], bem vindo
def saudacao(nome:str):
    print(
f"""--------------------------
--- ola {nome}, bem vindo ----
--------------------------
"""
    )
    print(" ")
saudacao("Gonçalo")

#3 crie uma função que permita criar uma var com a msg ola [nome], bem vindo
#    mostre a msg (fora da função)
def mensagem(nome:str):
    return(f"ola {nome}, bem vindo")
print("-----------------")

versao2 = mensagem("João")
novo = (versao2)

print("fora", novo)
print("-----------------")

#4 Cria uma função chamada dobro que receba um número e devolva o seu dobro.
def dobro(num):
    print(num * 2)
dobro(5)
print("-----------------")

#5 Cria uma função chamada media que receba dois números e devolva a média.
def media(num1, num2):
    soma = num1 + num2
    media = soma / 2
    return media
res = media(12, 16)
print(f"A média é", res)
print("-----------------")

#6 Cria uma função chamada par_ou_impar que receba um número e devolva:
#    "Par" se for par
#    "Ímpar" se for ímpar
def par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"
numero = 21
resultado = par_ou_impar(numero)
print(f"O número {numero} é", resultado)
print("-----------------")

#7 Cria uma função chamada maior que receba dois números e devolva o maior.
def maior(num1, num2):
    return max(num1, num2)
result = maior(6, 2)
print(f"O número Maior é", result )
print("-----------------")

#8 Cria uma função chamada positivo_negativo que receba um número e devolva:
#    "Positivo"
#   "Negativo"
#    "Zero"
def positivo_negativo(num):
    if num > 0:
        return "Positivo"
    elif num < 0:
        return "Negativo"
    else:
        return "Zero"
input_number = -15
resultado = positivo_negativo(input_number)
print(f"O número {input_number} é", resultado)
print("-----------------")

#9 Cria uma função chamada tabuada que receba um número e imprima a tabuada desse número (de 1 a 10).
def tabuada(n):
    print(f"Tabuada do número {n}:")
    for i in range(1, 11):
        calc = n * i
        print(f"{n} x {i} = {calc}")
tabuada(5)
print("-----------------")