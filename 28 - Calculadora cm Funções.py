import os
os.system("cls")

# 1 Etapa - Funções

def sair():
   exit()

def Somar (Numero1, Numero2):
  Resultado = Numero1 + Numero2
  return Resultado

def Subtrair (Numero1, Numero2):
  Resultado = Numero1 - Numero2
  return Resultado

def Multiplicar (Numero1, Numero2):
  Resultado = Numero1 * Numero2
  return Resultado

def Dividir (Numero1, Numero2):
  Resultado = Numero1 / Numero2
  return Resultado


# 2 Etapa - Abrindo a IA

print("Olá, que Bom te ver no Gemini Pro - Matemática.")
Calculadora = input("\nVocê deseja usar a Calculadora? s/n: ")

if Calculadora == "s":
  print("\nAbrindo a Calculadora")

else:
 print("Ok! Posso te Ajudar em Outra Coisa?")
 exit() 


# 3 Etapa - Usando a Calculadora 

Numero1 = int(input("Digite o 1°Numero: "))
Numero2 = int(input("Digite o 2°Numero: "))

print("\nEscolha a Operação: ")
print("1: Soma")
print("2: Menos")
print("3: Multiplicar")
print("4: Divisão")

Operação = input("\nDigite a Operação que Desejas: ")

if Operação == '1':
 print(f"A Soma é: {Somar(Numero1, Numero2)}")

elif Operação == '2':
 print(f"A Subtração é: {Subtrair(Numero1, Numero2)}")

elif Operação == '3':
 print(f"A Multiplicação é: {Multiplicar(Numero1, Numero2)}")

elif Operação == '4':
 print(f"A Divisão é: {Dividir(Numero1, Numero2)}")

else:
  print("\nOperação Invalida!")
  input("Pressione ENTER para Sair ...")
  exit()