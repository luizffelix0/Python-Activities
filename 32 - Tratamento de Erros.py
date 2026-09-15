import os
os.system("cls")

# ================
# 1 Etapa - Titulo

print(""" 

█▀▀ ▄▀█ █░░ █▀▀ █░█ █░░ ▄▀█ █▀▄ █▀█ █▀█ ▄▀█
█▄▄ █▀█ █▄▄ █▄▄ █▄█ █▄▄ █▀█ █▄▀ █▄█ █▀▄ █▀█ """)
# ============================================

# =================================================
# 2 Etapa - Calculo

while True:
    try:
        num1 = int(input("\nDigite um Numero: "))
        num2 = int(input("Digite mais um Numero: "))
        Resultado = num1 + num2
        Resultado = 10 / 0

        print(f"O Resultado é: {Resultado}")
        input("Press ENTER to Continue...")

    except ValueError as erro:
        print(f"\nMensagem de Erro:{erro}")
        print("Valores de Entrada devem ser Numeros Inteiros!")
    except ZeroDivisionError:
        print("Não é possivel Dividir por Zero")
        continue
# ============================================================