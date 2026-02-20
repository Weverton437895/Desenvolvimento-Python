"""
Trabalho 01 - Introdução ao Python
Gerenciador de Mochila para Viagens

Descrição: Sistema que controla peso máximo de bagagem (23kg)
permitindo adicionar itens e calculando espaço restante.
sem utilizar vetor.

Atividade: Desenvolvimento Web III-A947-T-D.S.M.-129-20261
"""

limitePeso = 23.0
pesoTotal = 0

nomeMochileiro = input("Qual é o seu nome? ")
print("Olá", nomeMochileiro)

itens = ""

while True:
    encerrar = input("Digite fim para encerrar ou Enter para continuar: ")
    if encerrar == "fim":
        break

    item = input("Digite o nome do item: ")
    pesoItem = float(input("Digite o peso do item em kg: "))

    if pesoTotal + pesoItem <= limitePeso:
        pesoTotal += pesoItem
        itens += item + "\n"
        print("Item adicionado!")
    else:
        print("Peso ultrapassa o limite")

    if pesoTotal == limitePeso:
        print("Limite atingido!")
        break

espacoRestante = limitePeso - pesoTotal

print("Nome:", nomeMochileiro)
print("Peso total:", pesoTotal, "kg")
print("Espaço restante:", espacoRestante, "kg")
print("Itens adicionados:")
print(itens)
