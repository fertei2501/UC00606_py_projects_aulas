"""

Cria uma função validarPassword(password) que:
chama as funções:
        temTamanhoMinimo(p) → mínimo 8 caracteres
        temNumero(p) → contém pelo menos 1 número
        temMaiuscula(p) → contém pelo menos 1 letra maiúscula

A função principal só retorna true se todas as validações passarem

"""
def tamanhoMinimo(p):
    return len(p) >= 8
def temNumero(p):
    return any(char.isdigit() for char in p)
def temMaiuscula(p):
    return any(char.isupper() for char in p)
def validarPassword(password):
    if tamanhoMinimo(password) and temNumero(password) and temMaiuscula(password):
        return "Password válida"
    else:
        return "Password inválida, não cumpre os parâmetros de segurança"
print(validarPassword("Senha123"))
print("-----------------")

"""
Cria uma função validarEmail(email) que:
chama as funções:

    temArroba(e) → verifica se tem @
    temEndereco(e) -> verifica se tem txt abtes da arroba
    temDominio(e) → verifica se tem .com, .pt, etc.
    naoTemEspacos(e) → não pode conter espaços
A função principal só retorna true se todas as validações forem cumpridas
"""

def temArroba(e):
    return "@" in e
def temEndereco(e):
    # Divide o email no @ e vê se a primeira parte tem texto
    partes = e.split("@")
    return len(partes[0]) > 0
def temDominio(e):
    # Verifica se termina com algum dos domínios comuns
    return e.endswith(".com") or e.endswith(".pt") or e.endswith(".org")
def naoTemEspacos(e):
    return " " not in e
def validarEmail(email):
    # Só retorna True se passar em todos os testes
    if temArroba(email) and temEndereco(email) and temDominio(email) and naoTemEspacos(email):
        return "Email válido!"
    else:
        return "Email inválido!"

# Teste
email_utilizador = input("Escreve o teu email: ")
print(validarEmail(email_utilizador))

