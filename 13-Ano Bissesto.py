import os
os.system("cls")

# 1 Etapa - Analize do Calendario

print("Calendario")
    
# 2 Etapa - Verificação

ano = int(input("Digite o Ano: "))

if ano %4 == 0:
    print(f"É Bissexto")

else:
    print(f"Não é Bissexto")