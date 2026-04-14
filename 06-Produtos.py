import os
os.system("cls")

print("\nOlá, Seja Bem-Vindo ao Mercado Livre!")

# 1 Etapa - Descrição do Produdo, Preço e Quantidade

Produto = str(input("\nO Que é o Produto: "))
Quantidade = float(input("\nQuantidade de itens: "))
Preço = float(input("\nPreço do Produto: ").replace(',', '.'))
Descrição = str(input("\nBreve descrição: "))

# 2 Etapa - Calculo dos Produtos

Total = Quantidade * Preço

if Quantidade <= 5:
# 2% de desconto
    Preço_Final = Total * 0.02
    print(f"\nO Desconto é {Preço_Final:.2f}")

elif Quantidade > 5 and Quantidade <= 10:
# 3% de desconto
    Preço_Final = Total * 0.03
    print(f"\nO Desconto é {Preço_Final:.2f}")

else: 
# 5% de desconto
    Preço_Final = Total * 0.05
    print(f"\nO Desconto é {Preço_Final:.2f}")
   
# 3 Etapa - Preço Comparativo

valor_desconto = Total - Preço_Final
print("\nO Preço com Desconto é: R$",valor_desconto)

print(f"\nO Total Bruto era: R$ {Total:.2f}")

print("=" * 30)
print(f"\n É Hora das Compras (;")