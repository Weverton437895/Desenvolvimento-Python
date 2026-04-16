from quiz import Quiz

while True:
    print("\nSistema QUIZ")
    print("1-iniciar")
    print("2-sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        nome = input("\nDigite seu nome: ")
        quiz = Quiz(nome)
        quiz.iniciarQuiz()

    elif opcao == "2":
        print("Saindo")
        break

    else:
        print("Opção inválida!\n")