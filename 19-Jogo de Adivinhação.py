import os
import random
os.system("cls")

# 1 Etapa - Adivinhe um Numero

print("\nJogo de Advinhação")

numero_secreto = random.randint(1,10)

Palpite = int(input("\nDe um Palpite:"))

# 2 Etapa - Você Acertou ?!?

if(Palpite == numero_secreto):
    print("Você Acertou!")

elif(Palpite > numero_secreto):
    print("O número está abaixo do seu palpite")

elif(Palpite < numero_secreto):
    print("Seu Palpite é menor")

# 3 Etapa - E o Numero Secreto éééééé:

print(f"\nO Numero Secreto é: {numero_secreto}")