"""
Trabalho 03 - Funções e Lista
Identificador de números primos
 
Descrição: Solicite ao usuário dois números inteiros positivos (início e fim de um intervalo).
Utilize uma função chamada eh_primo(numero) que retorne True se o número for primo e False caso contrário.
Utilize um laço while para percorrer o intervalo informado.
Conte quantos números primos existem no intervalo.
  
Atividade: Desenvolvimento Web III-A947-T-D.S.M.-129-20261 """

num1 = int(input("Digite o primeiro número inteiro positivo: "))
num2 = int(input("Digite o ultimo número inteiro positivo: "))

def eh_primo(numero):
    if numero <= 1:
        return False
    i = 2
    while i < numero:
        if numero%i == 0:
            return False
        i+=1

    return True
    
i = num1
contador = 0
maior_primo = 0

while i <= num2:
    if eh_primo(i):
        contador += 1
        maior_primo = i
        
    i += 1

print("Existem ",contador," Números primos")

if maior_primo >= 2:
    print("Maior primo do intervalo:", maior_primo)
else:
    print("Não existe primo nesse intervalo.")