import os
os.system ("cls")

#1 Etapa - Recebendo a Cor

print("\nBem Vindo ao Detran")
Semaforo = print("\nCor do Farol?")

print("Verde")
print("Amarelo")
print("Vermelho")

Cor_do_Semaforo = input("\nDigite a Cor do Farol: ")

#2 Etapa - Analizando a Cor

if Cor_do_Semaforo == 'Verde':
    print("Pode Passar")

elif Cor_do_Semaforo == 'Amarelo':
    print("Atenção!")

else:
    print("Dessacelere e PARE!")