import os
os.system ("cls")

#1 Etapa - Chegando no Pedagio

print("Bem Vindo ao Pedagio da AUTOBAN!")
input("\nVocê está indo a onde? ")

#2 Etapa - Veiculo

print("\nSelecione seu Veiculo:")
print("\nCarro")
print("Moto")
print("Caminhão")

Veiculo = input("\nSelecione o seu Veiculo: ")

#3 Etapa - Taxa para pagar sobre 'X' Veiculo

if Veiculo == 'Carro':
    print("Pague 10R$")

elif Veiculo == 'Moto':
    print("Pague 5R$")

else:
    print("Pague 20R$")