import os
os.system("cls")

# 1 Etapa - Ajuda no Estudo

print("\nOi, sou seu assistente de Estudo")

Materia = input("Qual Materia você estudo: ")

# 2 Etapa - Quanto Tempo você Estudou Essa Materia?

Tempo = float(input("Quanto tempo? "))  

# 3 Etapa - Você estudou o suficiente

if Tempo < 2:
    print("\nVocê Estudou muito Pouco, estuda mais (:, Conhecimento nunca é pouco")

elif Tempo <4:
    print("Você estudo o Suficiente, Mais pode melhorar |:")

else:
    print("\n Você Estudou Muito, Estou Feliz por Você")