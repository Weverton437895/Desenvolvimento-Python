import random

opcoes = ["pedra", "papel", "tesoura"]

while True:
    usuario = input("Escolha [pedra, papel ou tesoura]: ").lower()

    bot = random.choice(opcoes)

    if usuario == bot:
        print("O bot escolheu ",bot,"O jogo ficou empatado")
    elif(usuario == "papel" and bot == "pedra") or (usuario == "tesoura" and bot == "papel") or (usuario == "pedra" and bot == "tesoura"):
        print("O bot escolheu ",bot,"Você venceu")
    else:
        print("O bot escolheu ",bot,"Você perdeu")

    sair = input("Digite sair para encerrar o jogo. Enter para continuar.").lower()

    if sair == "sair":
        print("Sistema encerrado. ")
        break


