import os
import random  
os.system ("cls")

#Este é so um sistema de Batalha Pokemon
#1 Etapa - Escolha seu Pokemon
print("\nSeu Rival quer Batalhar com Você!")
print("Escolha o 'Inicial'")

print("1: Blastoise")
print("2: Venossaur")
print("3: Charizard")
Pokemon_do_Treinador = input("\nEscolha o Inicial: ")
Pokemon_do_Rival = "Fraqueza do Seu Pokemon"

if Pokemon_do_Treinador == '1':
    Pokemon_do_Rival = '2'
    print("\nSeu Rival Escolheu Venossaur")

elif Pokemon_do_Treinador == '2':
    Pokemon_do_Rival = '3'
    print("\nSeu Rival Escolheu Charizard")

elif Pokemon_do_Treinador == '3':
    Pokemon_do_Rival = '1'
    print("\nSeu Rival Escolheu Blastoise")

#2 Etapa - Informacões Essencias

Vida_do_Treinador = 100
Vida_do_Rival = 100
Poção = 10
Qntd_Poção = 5
Max_Potion = True #Só o Rival pode usar!

while Vida_do_Treinador > 0 and Vida_do_Rival > 0:

# 3 Etapa - Sistema de Batalha

    print("\n1: Ataque") #Você tem 100 de Hp
    print("2: Curar") #Use com Cautela
    print("3: Fugir") #Ultimo Recurso

    Ação = input("\nO Que vai Fazer? ")

    Atk_do_Treinador = random.randint(10,90)
    Atk_do_Rival = random.randint(10,90)

    # 4 Etapa - Batalha Pokemon!

    if Ação == '1' and Pokemon_do_Treinador == '1':
                if Vida_do_Rival > 0:
                 Vida_do_Treinador = Vida_do_Treinador - Atk_do_Rival
                Vida_do_Rival = Vida_do_Rival - Atk_do_Treinador
                print(f"\nBlastoise usou Hydro Canon, causando {Atk_do_Treinador} de dano |  Venossaur tem {Vida_do_Rival} de Hp")
                print(f"O Rival Atacou! Venossaur usou Solar Bean, causando {Atk_do_Rival} de dano |  Blastoise tem {Vida_do_Treinador} de Hp.")
                

    elif Ação == '1' and Pokemon_do_Treinador == '2':
                if Vida_do_Rival > 0:
                 Vida_do_Treinador = Vida_do_Treinador - Atk_do_Rival
                 Vida_do_Rival = Vida_do_Rival - Atk_do_Treinador
                 print(f"\nVenossaur usou Solar Bean, causando {Atk_do_Treinador} de dano | Charizard tem {Vida_do_Rival} de Hp")
                print(f"O Rival atacou! Charizard usou Flamethrower, causando {Atk_do_Rival} de dano |  Venossaur tem {Vida_do_Treinador} de Hp.") 
               
                
    elif Ação == '1' and Pokemon_do_Treinador == '3':
                 if Vida_do_Rival > 0:
                  Vida_do_Treinador = Vida_do_Treinador - Atk_do_Rival
                 Vida_do_Rival = Vida_do_Rival - Atk_do_Treinador
                 print(f"\nCharizard usou Flamethrower, causando {Atk_do_Treinador} de dano |  Blastoise tem {Vida_do_Rival} de Hp")
                 print(f"O Rival Contra Atacou! Blastoise usou Hydro Canon, causando {Atk_do_Rival} de dano |  Charizard tem {Vida_do_Treinador} de Hp.")

    if Vida_do_Rival <= 0 :
       print("\nVocê Venceu! Agora és o Campeão Mundial!") 
       break     

    if Vida_do_Treinador <= 0:
           print("\nVocê foi Derrotado! Volte ao Centro Pokemon!")
           
    elif Vida_do_Rival < 10 and Max_Potion == True:
        Vida_do_Rival = 100
        Max_Potion = False #Já Usou Uma Vez!
        print(f"\n Rival Recuperou o Hp, agora ele tem: {Vida_do_Rival}")
     
    elif Ação == '2':
       Vida_do_Treinador = Vida_do_Treinador + Poção
       Qntd_Poção -= 1
       if Vida_do_Treinador > 100:
        Vida_do_Treinador = 100
       print(f"\nVocê Curou! Agora tens {Vida_do_Treinador} de Hp! Agora tens {Qntd_Poção} de Poção.")  
       
    elif Ação == '3':
           print("\n'Que Covarde hahahaHAHAHAHAH! - Rival' ")
           break
    
# 5 Etapa - Fim de Jogo