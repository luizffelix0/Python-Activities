import os
os.system("cls")

# 1 Etapa - Fazendo a Lista

print("Manipulando Listas/Arrays")

numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ["Luiz", "Maria", "Giovanni", "Graciele", "Flavio"]

print("\nListas Iniciais")
print(nomes)
print("=================================")
print(f"\nNome da Posição 1 da Lista: {nomes[1]}")

# 2 Etapa - Aterações na Ordem da Lista

nomes[1] = "Joaquim"
print(f"\nLista Nova: {nomes}")

# 3 Etapa - Um Toque Final

nome = input("\nDigite um Nome: ")
nomes.append(nome)

print("Lista Atualizada")
print(nomes)

# 4 Etapa - Adicionar mais Nomes

nomes.insert(2, "Michael Jackson: Rei do Pop!")
print("Lista Atualizada")
print(nomes)

# 5 Etapa - Removendo Nomes
del nomes[3]
print("Lista Atualizada")
print(nomes)