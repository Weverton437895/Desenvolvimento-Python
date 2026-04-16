from perguntas import Perguntas

class Quiz:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciarQuiz(self):
        for pergunta in Perguntas.perguntas:
            self.perguntar(pergunta)

        print("\nResultado Final")
        print(f"Jogador: {self.nome}")
        print(f"Acertos: {self.pontuacao}")


    def perguntar(self, pergunta):
        print(pergunta["enunciado"])

        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        resposta = self.responder()

        if resposta.upper() == pergunta["resposta"]:
            self.pontuacao += 1
            print("Correto")
        else:
            print("Errado")

    def responder(self):
        return input("\nSua resposta: ")