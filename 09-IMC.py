import os
os.system("cls")

# 1 Etapa - Sabendo seu Peso

Seu_Peso = float(input("\nDigite seu Peso: ").replace(',', '.'))

Sua_Altura = float(input("\nDigite sua Altura: ").replace(',', '.'))

Resultado = "Sim"

# 2 Etapa - Calculando o seu IMC


iMC = Seu_Peso / (Sua_Altura * Sua_Altura)
print(f"\nSeu iMC é {iMC:.2f}")

# 3 Etapa - Classificação de seu iMC

if  iMC <= 16.9:
    print("\nVocê esta  Muito Abaixo do Peso")

elif iMC > 17 and iMC <= 18.4:
    print("\nVocê está Abaixo do Peso")

elif iMC > 18.5 and iMC <= 24.9:
    print("\nVocê está com o Peso Normal")

elif iMC > 25 and iMC <= 29.9:
    print("\nVocê está com o Acima do Peso")

elif iMC > 30 and iMC <= 34.9:
    print("\nVocê tem Obesidade Grau I")

elif iMC > 35 and iMC <= 40:
    print("\nVocê tem Obesidade Grau II")

elif iMC > 40:
    print("\nVocê tem Obesidade Grau III")