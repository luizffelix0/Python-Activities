import os
os.system("cls")

# 1 Etapa - Entrar no Site

print("\nOlá! Faça seu Login")

# 2 Etapa - Digite seu Login e Senha

Login = input("Digite seu Login: ")
Senha = input("Digite sua Senha: ")

# 3 Etapa - Verificação

if Login == "Admim" and Senha == "123":
    print("\nAcesso Liberado! Olá Novamente")

else:
    print("\nAcesso NEGADO! Tente Novamente.")