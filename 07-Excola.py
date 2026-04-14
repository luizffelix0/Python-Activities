import os
os.system("cls")

# 1 Etapa - Conhecendo o Professor

print("\nOlá, Bem-Vindo a Secretaria do Professor do SESi")

print("\nSelecione seu Nivel de Professor:")

print("1: Nivel 1")      
print("2: Nivel 2")
print("3: Nivel 3")

Nivel = input("\nDigite o Nivel: ")

if Nivel == '1':
    Salario_Por_Hora = 12.00

elif Nivel == '2':
     Salario_Por_Hora = 17.00

elif Nivel == '3':
     Salario_Por_Hora = 25.00

# 2 Etapa - Sabendo sua Rotina

Carga_Horaria = float(input("\nSua Carga Horaria (Ex:6 horas): "))

Carga_Diaria = float(input("\nSua Carga Diaria: "))

# 3 Etapa - Calculando seu Salario

Salario_Semanal = Salario_Por_Hora * Carga_Horaria * Carga_Diaria
print(f"\nSeu Salário Semanal é de R$ {Salario_Semanal:.2f}")

Salario_Mensal = Salario_Semanal * 4.5
print(f"\nSeu Salário Mensal é de R$ {Salario_Mensal:.2f}")