import os
os.system("cls")

# 1 Etapa - Combustivel no Carro/Moto

print("\nBem vindo ao Shell Box")

Quilometros = int(input("\nQuantos Quilometros Você Percorreu? "))
Litros = int(input("\nQuantos Litros Você Gastou? "))

# 2 Etapa - Consumo

Consumo = Quilometros / Litros
print("\nVocê Gastou",Consumo, "a cada Km Rodado")
