palavra = input("Digite uma palavra para ver quantas vogais possui: ").lower()

vogais = ["a","e","i","o","u"]

contador = 0

for vog in palavra:
    if vog in vogais:
         contador+=1
   
if contador >= 1:
     print("Tem ",contador," Vogais na palavra")
else:
     print("Não a nenhuma vogal na palavra")
        