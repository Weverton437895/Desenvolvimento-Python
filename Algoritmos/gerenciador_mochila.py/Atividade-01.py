"""
Trabalho 01 - Introdução ao Python
Gerenciador de Mochila para Viagens

Descrição: Sistema que controla peso máximo de bagagem (23kg)
permitindo adicionar itens e calculando espaço restante.

Curso: Desenvolvimento Web III-A947-T-D.S.M.-129-20261
Autor: [Seu Nome]
Data: 18/02/2026
"""

limitePeso = 23.00
pesoTotal = 0
quantoFalta = 0

nomeMochileiro = input("Qual é o seu nome? ")
print("Olá", nomeMochileiro)

nomeItem = []

while True:
   encerrarSelecao = input("Digite fim para encerrar a seleção. Enter para continuar: ")
   if encerrarSelecao == "fim":
    break

   print("------------------------------------------------------------------------------")
   item = input("Digite o nome do item que deseja levar: ")
   pesoItem = float(input("Digite o peso do item que deseja levar em kg: "))
   print("------------------------------------------------------------------------------")

   if pesoTotal + pesoItem <= limitePeso:
     pesoTotal += pesoItem
     nomeItem.append(item)
     quantoFalta = limitePeso - pesoTotal
     print("O ",item," Foi adicionado. Peso do item ",pesoItem,"kg. Peso atual da mochila ",pesoTotal)
     print("Falta ",quantoFalta,"kg, Para chegar ao peso total da mochila")

     if pesoTotal == limitePeso:
      print("Limite de peso atingido.")
      break
     
   else:
     print("Item selecionado ultrapassa o limite de peso da mochila, item removido")
     print("Peso atual é ",pesoTotal,"Kg. Item removido")

quantoFalta = limitePeso - pesoTotal

print("O nome do mochileiro é ",nomeMochileiro,"\nO peso total dos itens é ",pesoTotal,"Kg\nEspaço restante na mochila é ",quantoFalta,"Kg")
print("------------------------------------------------------------------------------")
print("Itens adicionados")
for nome in nomeItem:
  print(nome)