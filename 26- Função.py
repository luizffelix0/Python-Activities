import os
os.system("cls")

# 1 Etapa - Criando uma Função

def escreva():
    print("\nOlá Mundo")

# Chamando a Função
escreva()

# 2 Etapa - Função com Parametro

def Exibir_Dados(Nome,Idade,Email):
    print(f"Nome: {Nome}")
    print(f"Idade: {Idade}")
    print(f"\nEmail: {Email}")
    print("=" * 50)

# Chamando a Função
escreva()

# 3 Etapa - Exibir 

Exibir_Dados("Felix", 15, "Luiz0F@Gmail.com.br")

# 4 Etapa - Criando uma Função com Retorno

def somar(num1,num2):
    resultado = num1 + num2
    return resultado

# Chamando a Função com Retorno
somar(10,20)