import os
import time
os.system("cls")

#1 Etapa - Introduzindo o Sistema de Conversor de Moedas

#Criando a função main - principal
def main():
    limpar_tela()
#Criando a funcao limpar tela
def limpar_tela():
    os.system("cls")
#Função Sair
def sair():
   exit()

#1 Etapa - Menus da Bovespa e Conversor

#Menu da Bovespa
print("\nOlá, Bem Vindo a Bovespa.")
print("\n[1] - Area do Investidor")
print("[2] - Serviços e Produtos")
print("[3] - Regulação")
print("[4]- Sair")

#Solicitar que o Usuario escolha uma Opção do Menu
Menu = int(input("Selecione uma dessas Opções: "))

#Menu do Conversor
Executar_Novamente = "sim"

while (Executar_Novamente == "sim"):
    def exibir_menu_Conversor():
        print("=== Conversor de Moedas ===")
        print("\n[1] - Converter DOLAR -> REAL")
        print("[2] - Converter REAL -> DOLAR")


    #Continuação do Menu da Bovespa
    if Menu == 1:
        Resposta = input("\nVoce escolheu Area do Investidor, Quer Converter Moedas Para Investir? S/N: ").upper()

        if Resposta == 'S':
            time.sleep(1)
            limpar_tela()
            exibir_menu_Conversor()
        elif Resposta == 'N':
            print("Ok, Volte Mais Tarde.")
            exit()

    elif Menu == 2:
        print("Para Mais Informações, acesse nosso Site:'https://www.b3.com.br/';")

    elif Menu == 3:
        print("Para Mais Informações, acesse nosso Site:'https://www.b3.com.br/';")

    else:
        limpar_tela()
        exit()

    #2 Etapa - Funções para Converter

    #Função Converter de dolar para real
    def converter_dolar_para_real(quantia_dolar, cotacao):
        total_reais = quantia_dolar * cotacao
        return total_reais
    
    #Função Converter de Real para Dolar
    def converter_real_para_dolar(quantia_real, cotacao):
        total_dolares = quantia_real / cotacao
        return total_dolares
    
    #3 Etapa - Introduzindo o Sistema de Conversor de Moedas
        # Solicitando a opção do usuário

    opcao = int(input("Escolha uma opção: "))
        
    if(opcao == 1):
                quantia_dolar = float(input("Informe a quantia de dolares:"))
                cotacao = float(input("Informe a cotação:").replace(",", "."))
                resultado = converter_dolar_para_real(quantia_dolar, cotacao)
                print(f"\nO total da conversão é: R${resultado}")
                input("Pressione ENTER para continuar...")

    elif(opcao == 2):
                quantia_reais = float(input("Informe a quantia de reais:"))
                cotacao = float(input("Informe a cotação:").replace(",","."))
                resultado = converter_real_para_dolar(quantia_reais, cotacao)
                print(f"\nO total da conversão é: ${resultado}")
                input("Pressione ENTER para continuar...")

            
    resposta = input("\nVocê gostaria de Executar Novamente? (sim ou não): ")
    if resposta == 'não':
            print("Ok, Volte Sempre!")
        #Chamando a função principal do programa
    main()