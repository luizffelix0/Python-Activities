import os
os.system("cls")

print("""  
██████████████████████████████████████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█▄─▄▄▀█─▄▄▄─██▀▄─██▄─▄▄▀█─▄▄─███▄─▄███▄─▄█▄─█─▄█▄─▄▄▀█▄─▄▄─█
██─█▄█─███─▄█▀██─▄─▄█─███▀██─▀─███─██─█─██─████─██▀██─███▄▀▄███─▄─▄██─▄█▀█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▄▀▄▄▄▀▀▀▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀ """)
input("\nPress ENTER to continue ...")

# ====================================================================
# 1 Etapa - Descrição do Produdo e o Preço

while True:
    os.system("cls")
    print("Diga sobre o Seu Produto")
    Produto = str(input("\nO Que é o Produto: "))
    Preco = float(input("\nPreço do Produto: ").replace(',', '.'))

    input("\nPress ENTER to continue ...")

    # ===============================================================

# 2 Etapa - Abrir o Arquivo

    Arquivo = open("Produtos.txt", "a")
    Arquivo.write(f"\n === Dados do Produto ===")
    Arquivo.write(f"\nNome: {Produto}")
    Arquivo.write(f"\nPreco: {Preco} \n")
    Arquivo.write("=" * 100 )
    Arquivo.close()
        
#===================================================