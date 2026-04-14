
import os

os.system("cls")

#1 passo - Declarar variaveis e realizar entrada de dados
print("Seja bem-vindo ao Seu Boletim!")

Nota01 = int(input("Digite o primeiro valor:"))
Nota02 = int(input("Digite o segundo valor:"))
Nota03 = int(input("Digite o terceiro valor:"))

#2 passo - Processamento
Media = (Nota01 + Nota02 + Nota03 ) /3

#3 passo - Exibir a saída (resultado)
print("O Resultado é: ", Media)

if(Media>=7):
    print("Você Passou, Parabéns!")

elif(Media>=4 and Media<=6):
    print("Você está de Recuperação! Que Pena...")

else:
    print("Você é... BURRO PRA KRLHO")