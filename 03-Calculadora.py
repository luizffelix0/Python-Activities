import os
os.system("cls")

# 1 Etapa - Entrada

print("Calculadora")

numero01 = float(input("Digite um Numero:"))

# 2 Etapa - Processamento

print("\nEscolha a Operação: ")
print("+: Soma")
print("-: Menos")
print("*: Multiplicar")
print("/: Divisão")

Operação = input("\nDigite a Operação que Desejas: ")

# 3 Etapa - Valores Digitados

numero02 = float(input("\nDigite um Numero:"))

# 4 Etapa - Calculo das Operações

if Operação == '+':
    resultado = numero01 + numero02
    print("A Resposta é: ", resultado)

elif Operação == '-':
    resultado = numero01 - numero02
    print("A Resposta é ", resultado)

elif Operação == '*':
    resultado = numero01 * numero02
    print("A Resposta é ", resultado)

elif Operação == '/':
    if numero01 != 0:
     if numero02 != 0:
      resultado = numero01 / numero02
      print("A Resposta é ", resultado)
    else: 
      print("\nErro: Não é possível dividir por zero!")

else:
    print("\nOperação inválida! Por favor, tente novamente.")
