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