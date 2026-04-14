import os
os.system("cls")

#1 Etapa - Tabuada

print("Exemplo Tabuada com While")

Numero = int(input("\nDigite um Numero: "))
Limite = int(input("Digite o Limite da Tabuada: "))

#2 Etapa - Calculando

contador = 0
while(contador <= Limite):
    print(f"{Numero} X {contador} = {Numero * contador}")
    contador+=1