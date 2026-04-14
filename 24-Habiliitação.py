import os
os.system ("cls")

#1 Etapa - CNH: Carteira de Motorista

print("Exemplo de Habilitação com While")

resposta = "sim"

while (resposta == "sim"):


    Nome = input("\nDigite seu Nome: ")
    iDade = int(input("Digite sua iDade: "))

    #2 Etapa - Verificando a iDade

    if iDade >= 18:
        Habilitação = int(input("Possui Habilitação para Dirigir? Sim(1) ou Não(2): "))

    #3 Etapa - Autorizando 

        if Habilitação == 1:
            print("Você Pode Dirigir!")

        else:
            print("Você não pode Dirigir.")

    else:
        print("Você é Menor de iDade")

    resposta = input("\nVocê gostaria de Executar Novamente? (Sim ou Não): ")
    if resposta == 'Não':
        print("Ok, Volte Sempre!")