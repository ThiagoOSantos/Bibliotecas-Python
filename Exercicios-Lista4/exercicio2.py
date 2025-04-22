import random

def dado6():
    while True:

        print("Bem vindo aos jogos dadais! Vamos ao primeiro lançamento")
        numero = random.randint(1,6)
        print(f"O primeiro lado sorteado é: {numero} \n")
        opcao = input(("Deseja jogar novamente?"))
        if opcao == "nao":
            break
