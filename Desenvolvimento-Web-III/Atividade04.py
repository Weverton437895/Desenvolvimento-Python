"""
Trabalho 04 - Coleção
Agenda Telefônica com Dicionário
 
Descrição: Desenvolver um programa em Python que simule uma agenda telefônica simples,
utilizando exclusivamente um dicionário para armazenar os contatos.

Cada contato é armazenado como:
- Chave: nome do contato
- Valor: número de telefone

Funcionalidades implementadas:
1 - Cadastrar contato (com possibilidade de atualização)
2 - Buscar contato
3 - Excluir contato
4 - Listar todos os contatos
5 - Encerrar o programa
  
Atividade: Desenvolvimento Web III-A947-T-D.S.M.-129-20261
"""

contatos = {}

while True:
    print("-------------------------------------------------------")
    print("\n1 - Cadastrar")
    print("2 - Buscar")
    print("3 - Excluir")
    print("4 - Listar")
    print("5 - Sair")
    print("\n-------------------------------------------------------")

    opcao = int(input("Escolha o número da opção desejada: "))

    if opcao == 1:
        nome = input("Digite o nome para salvar o contato: ").lower()
        numero = input("Digite o número do contato: ")
        if nome in contatos:
            print("\nContato já existe. ")
            atualizar = input("Deseja atualizar? [S/N]: ").lower()
            if atualizar == 's':
                contatos[nome] = numero
                print("\nContato atualizado. ")
        else:
            contatos[nome] = numero
            print("\nContato cadastrado. ")
    elif opcao == 2:
        busca = input("Digite o nome do contato para buscar: ").lower()
        if busca in contatos:
            print("\nContato encontrado: ")
            print(f"Número do contato é {contatos[busca]}")
        else:
            print("\nContato não foi encontrado.")
    elif opcao == 3:
        excluir = input("Informe o nome do contato que deseja excluir: ").lower()
        if excluir in contatos:
            del contatos[excluir]
            print("\nContato excluido.")
        else:
            print("\nContato não encontrado.")
    elif opcao == 4:
        if contatos:
            print("\nContatos salvos.")
            for nome, numero in contatos.items():
                print(f"Nome e número do contato: {nome} - {numero}")
        else:
            print("Nenhum contato salvo. ")
    elif opcao == 5:
        print("Programa encerrado. ")
        break
