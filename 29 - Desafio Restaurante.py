import os 
os.system("cls")

# 1 Etapa - Fazendo as Funções

def sair():
   exit()

def Dividir (Preço, Qntd_de_Pessoas):
  Total_por_Pessoa_a_Pagar = Preço / Qntd_de_Pessoas
  return Total_por_Pessoa_a_Pagar


# 2 Etapa - Recebendo os Comandos
print("Olá, Seja Bem Vindo ao App Minha Conta!")
Ação = input("\nDeseja Fazer um Pagamento, S/N: ").lower()

if Ação == 's':
    print("\nDirecionando Para a Area de Pix")
    input("Pressione ENTER para fazer o Pagamento ...")


else:
    print("Voltando para o Menu Principal do App ...")
    exit()

# 3 Etapa - Pagamento

Qntd_de_Pessoas = int(input("\nInforme a Quantidade de Pessoas: "))
Preço = int(input("\nDigite o Preço: "))

print(f"O Total a Pagar, Por Pessoa, é: {Dividir(Preço, Qntd_de_Pessoas)}")
Pagar_a_Conta = input("Deseja Efetuar o Pagamento? S/N: ").lower()

if Pagar_a_Conta == 's':
   print("\nEfetuando o Pagamento em Instantes ...")
   int(input("\nDigite Sua Senha: "))
   print("Pagamento Conluido!")

elif Pagar_a_Conta == 'N':
   print("OK, Posso Ajudar em algo mais?")
   exit()