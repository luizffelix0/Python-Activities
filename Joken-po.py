import os
import random
os.system("cls")

itens = ["Pedra", "Papel", "Tessoura"]
Ia = random.choice(itens)

print("Pedra, Papel ou Tessoura!")
player = input("escolha: ")

print("A Ia Escolheu:", Ia)


if player == Ia:
    print("Empate!")

elif player == "Pedra" and Ia == "Tessoura":
    print("Player Venceu!")

elif player == "Tessoura" and Ia == "Papel":
    print("Player Venceu!")

elif player == "Papel" and Ia == "Pedra":
    print("Player Venceu!")

else:
    print("A Ia Venceu! KAKAKAKAKAKAK 🤣")