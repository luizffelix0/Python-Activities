import os
os.system("cls")

#1 Etapa - Quantidade de Produto

print("\nBem Vindo a KABUM")
Produto = input("\nQual é o seu Produto? ")
Quantidade_em_Estoque = float(input("\nQuantos Produtos Você Quer? "))

#2 Etapa - Verificando o Estoque

if Quantidade_em_Estoque >5:
    print("\nProduto no Estoque!")

elif Quantidade_em_Estoque <5:
    print("\nProduto Baixo no Estoque")

