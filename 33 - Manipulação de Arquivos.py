import os
os.system("cls")

# ===================================
# 1 Etapa - Sistema para Cadastrar

print("\n === Bem Vindo ao Sistema de Cadastro ===")

while True:

    Nome = input("\nDigite seu Nome: ")
    Email = input("Digite seu Email: ")
    Celefone = int(input("Digite seu Telefone: "))
    Idade = int(input("Digite seu Idade: "))
    cpf = int(input("Digite seu CPF: "))

    input("\nPress ENTER to continue ...")
    # =====================================================

    # =====================================================
    # 2 Etapa - Abrir o Arquivo

    Arquivo = open("Contatos.txt", "a")
    Arquivo.write(f"\n === Dados do Cliente ===")
    Arquivo.write(f"\nNome: {Nome}")
    Arquivo.write(f"\nEmail: {Email}")
    Arquivo.write(f"\nTelefone {Celefone}")
    Arquivo.write(f"\nIdade: {Idade}")
    Arquivo.write(f"\nCPF: {cpf}")
    Arquivo.write("=" * 100)
    Arquivo.close()
    
#===============================================