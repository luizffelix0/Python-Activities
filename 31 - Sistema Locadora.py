import os

# ==========================
# 11 Etapa - Pior Filme
# =======================================================

def pior_filme(Filmes):
    return min(Filmes, key=lambda item: item["Media"])

# =======================================================
# 10 Etapa - Melhor Filme
# =======================================================

def melhor_filme(Filmes):
    return max(Filmes, key=lambda item: item["Media"])

# =======================================================
# 9 Etapa - Devolver o Filme
# ==================================================================================

def devolver_filme(Filmes):
    os.system("cls")
    print(" === Devolver Filmes ===")
    Titulo = input("Informe o Nome do Filme: ")

    for item in Filmes:
        if item["Titulo"].lower == Titulo.lower():
            
            for item in filmes:
                if item["Titulo"].lower() == Titulo.lower():
                 if item["Disponivel"] == False:
                  print(f"\nO filme estava com {item['Cliente']}")
                  nota = float(input("De uma nota de 0 a 10: "))
                  item["Avaliações"].append(nota)
                  item["Media"] = calcular_media(item["Avaliações"])
                  item["Classificacao"] = classificar_filmes(item["Media"])
                  item["Disponivel"] = True
                  item["Cliente"] = None
                  print("znFilme Devolvido")
                  print(f"A Nova Media do Filme é: {item['Media']}")
                  input("znPressione ENTER para a Continuação ...")

            else:
                print("\nEste filme está disponível.")

            return

# =============================================================================
# 8 Etapa - Alugar Filmes
# ========================================================

def alugar_filme(Filmes):

    os.system("cls")
    print(" === Aba: Alugueis de Filme ===")
    Titulo = input("\nInforme o Nome do Filme: ")
    Nome = input("Informe Seu Nome: ")

    for item in Filmes:

        if item["Titulo"].lower == Titulo.lower():
            #O Filme Existe?

            if item["Disponivel"] == True:

                item ["Cliente"] = Nome
                item ["Disponivel"] = False

                print("\nFilme Alugdo com Sucesso👍!")

            else:
                print(f"\nO Filme Esta alugado pelo {item['Cliente']}")

    input("\nPressione ENTER para Prosseguir ...")

# ========================================================================
# 7 Etapa - Media dos Filmes
# ================================

def classificar_filmes(media):
    if(media >= 8):
        return "Sucesso👍!"
    
    elif(media >= 5):
        return "Regular."
    
    else:
        return "Flop👎!"

# ===============================
# 6 Etapa - Calcular a Media
# =======================================================

def calcular_media(Avaliações):
    if len(Avaliações) == 0:
        return 0
    
    return round(sum(Avaliações) / len(Avaliações), 1)

# =======================================================
# 5 Etapa - Buscar Filme
# ======================================================

def buscar_filme(titulo, filmes):
    for item in filmes:
        if item["Titulo"].lower() == titulo.lower():
            return item
        else:
            return None

# ======================================================
# 4 Etapa - Catalogo de Filmes
# =========================================================

def exibir_catalogo(Filmes):
    print("\n=== Catálogo de Filmes ===")

    for item in Filmes:
        print(f"\nTitulo: {item["Titulo"]}")
        print(f"Genero: {item["Genero"]}")
        print(f"Classificação: {item["Classificação"]}")
        print(f"Avaliações: {len(item["Avaliações"])}")

        if item ["Disponivel"]:
            status = "Disponivel"
        else:
            status = f"Alugado por {item["Cliente"]}"

        print(f"Status: {status}")
        print("=" * 30)

# =========================================================
# 3 Etapa - Cadastrar Filme
# ==========================================

def cadastrar_filme():
    Titulo = input("\nTitulo do Filme: ")
    Genero = input("Gênero: ")

    Filme = {
         "Titulo" : Titulo,
         "Genero" : Genero,
         "Avaliações" : [],
         "Media" : 0,
         "Classificação" : "Sem Classificações.",
         "Disponivel" : True,
         "Cliente" : None
    }
    return Filme    

# ======================================================
# 2 Etapa - Menu: Adiministrador
# =================================================

def carregar_menu_adimim():
    os.system("cls")
    senha = input("Informe a Senha do Adimim: ")

    if senha != "123":
        print("ACESSO NEGADO!")
        return
    
    while True:
        print("\n=== Menu Adimin ===")
        print("\n[1] - Cadastrar Filme")
        print("[2] - Ver Catalogo")
        print("[3] - Top e Flop")
        print("[4] - Voltar")

        op = int(input("\nEscolha uma Opção: "))

        if (op == 1):
            os.system("cls")
            print("\n=== Cadastro de Filmes ===")
            Filme = cadastrar_filme()
            filmes.append(Filme)
            print("\nFilme Cadastrado!")
            input("Pressione ENTER para Seguir!")

        elif (op == 2):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione ENTER para Seguir!")

        elif (op == 3):
            os.system("cls")
            print(" === Filmes TOP & FLOP === ")
            print(f"O Melhor Filme é: {melhor_filme(filmes)}")
            print(f"O Pior Filme é: {pior_filme(filmes)}")
            input("Pressione ENTER pra Continuar ...")

        elif (op == 4):
            return

# ==================================================
# 2 Etapa - Menu: Cliente
# ==========================================================

def carregar_menu_cliente():
    while True:
        os.system("cls")
        print("\n=== Menu Cliente ===")
        print("\n[1] - Ver Catalogo")
        print("[2] - Buscar Filme")
        print("[3] - Alugar Filme")
        print("[4] - Devolver Filme")
        print("[5] - Sair")

        op = int(input("Escolha uma Opção: "))

        if (op == 1):
            os.system("cls")
            exibir_catalogo(filmes)
            input("Pressione ENTER para seguir")

        elif (op == 2):
            print("\n=== Encontre um Filme ===")
            Titulo = input("\nDigite o Nome do Filme: ")
            Filme = buscar_filme(Titulo, filmes)

            if Filme:
                print(f"Filme Encontrado: {Filme}")
            else:
                print("Filme não encontrado")
            input("Prossiga apertando ENTER ...")

        elif (op == 3):
            alugar_filme(filmes)

        elif (op == 4):
            devolver_filme(filmes)

        else:
            return
            

# =========================================================
# 1 Etapa - Sistema Principal
# ================================================

filmes = [
    {
        "Titulo": "Inception",
        "Genero": "Ficção Científica",
        "Avaliações": [],
        "Media": 0,
        "Classificação": "Sem Classificações.",
        "Disponivel": True,
        "Cliente": None
    },
    {
        "Titulo": "Titanic",
        "Genero": "Romance/Drama",
        "Avaliações": [],
        "Media": 0,
        "Classificação": "Sem Classificações.",
        "Disponivel": True,
        "Cliente": None
    },
    {
        "Titulo": "The Dark Knight",
        "Genero": "Ação",
        "Avaliações": [],
        "Media": 0,
        "Classificação": "Sem Classificações.",
        "Disponivel": True,
        "Cliente": None
    },
    {
        "Titulo": "Avengers: Endgame",
        "Genero": "Ação/Aventura",
        "Avaliações": [],
        "Media": 0,
        "Classificação": "Sem Classificações.",
        "Disponivel": True,
        "Cliente": None
    },
    {
        "Titulo": "Interstellar",
        "Genero": "Ficção Científica",
        "Avaliações": [],
        "Media": 0,
        "Classificação": "Sem Classificações.",
        "Disponivel": True,
        "Cliente": None
    }
]


while True:
    os.system("cls")
    print("\n=== Bem vindo a Locadora da Amazon ===")
    print("\n[1] - Entre em Cliente")
    print("[2] - Entre como Adiministrador")
    print("[3] - Sair")

    op = int(input("\nEscolha uma Opção: "))

    if (op == 1):
        print("\nVocê entrou como Cliente")
        carregar_menu_cliente()

    elif (op == 2):
        print("\nVocê entrou como Adiministrador")
        input("Pressione ENTER para Seguir!")
        carregar_menu_adimim()

    else:
        print("\nObrigador por usar o Serviços!")
        input("Press ENTER to Exit ...")
        break

# ====================================================