import os
os.system("cls")

#1 Etapa - RECEBA o Numero

Intervalo_Numerico = float(input("\nDigite um Numero: "))

#2 Etapa - Analizando o Numero

if Intervalo_Numerico > 10 and Intervalo_Numerico <=50:
    print("\nEstá entre 10 e 50")

else:
    print("Está Fora do Intervalo")