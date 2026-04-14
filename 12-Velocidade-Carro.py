import os
os.system("cls")

# 1 Etapa - Velocimetro

print("\n   Radar Semaforico")
print(" Limite 80km /h")
 
velocidade_km = float(input("\nQual sua Velocidade? "))


# 2 Etapa - Verificando a Velocidade

if velocidade_km > 80:
    print("Passou do Limite, Está Multado")

else:
    print("Você está no Limite")