"""
Trabalho 02 - Funções em Python
Minigame de adivinhação
 
Descrição: Desenvolver um programa que gere uma lista com cinco números aleatórios. 
Em seguida, o sistema deve solicitar ao usuário que informe cinco números e verificar 
quantos deles coincidem com os números gerados, exibindo ao final a pontuação obtida.
O programa deve conter duas funções:
Uma função responsável por gerar 5 números aleatórios.
Uma função responsável por verificar a quantidade de acertos do usuário.
  
Atividade: Desenvolvimento Web III-A947-T-D.S.M.-129-20261 """

import random

def GerarNumeros():
    numeros = []
    for i in range (5):
        sorteados = random.randint(1,10)
        numeros.append(sorteados)
    return numeros

def VerificarAcertos(numeros, usuario):
    contador = 0
    for numero in usuario:
        if numero in numeros:
            contador += 1
    
    return contador

usuario = []
print("Digite 5 números  para verificar quantos números coincidem com os números gerados")

for i in range(5):
    numero = int(input("Digite um número: "))
    usuario.append(numero)

numeros = GerarNumeros()

print("Números gerados pela maquina = ",numeros)
print("Números escholido pelo usúario = ",usuario)
print("Quantidade de números acertados = ",VerificarAcertos(numeros,usuario))

    
