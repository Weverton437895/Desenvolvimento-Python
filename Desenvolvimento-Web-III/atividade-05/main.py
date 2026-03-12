from livro import Livro, LivroDigital
from usuario import Usuario
from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:
    print("\n=== SISTEMA BIBLIOTECA ===")
    print("1 - Cadastrar Livro")
    print("2 - Cadastrar Usuário")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("5 - Listar Livros Disponíveis")
    print("6 - Listar Livros Emprestados")
    print("7 - Sair")

    op = input("Escolha: ")

    if op == "1":
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano = input("Ano: ")
        livro = Livro(titulo, autor, ano)
        biblioteca.adicionar_livro(livro)

    elif op == "2":
        nome = input("Nome: ")
        matricula = input("Matrícula: ")
        usuario = Usuario(nome, matricula)
        biblioteca.cadastrar_usuario(usuario)

    elif op == "3":
        for i, livro in enumerate(biblioteca.livros):
            print(i, livro)

        livro_index = int(input("Escolha o livro: "))
        for i, usuario in enumerate(biblioteca.usuarios):
            print(i, usuario)

        usuario_index = int(input("Escolha o usuário: "))
        biblioteca.usuarios[usuario_index].pegar_emprestado(
            biblioteca.livros[livro_index]
        )

    elif op == "4":
        for i, usuario in enumerate(biblioteca.usuarios):
            print(i, usuario)

        usuario_index = int(input("Usuário: "))
        usuario = biblioteca.usuarios[usuario_index]

        for i, livro in enumerate(usuario.livros_emprestados):
            print(i, livro)

        livro_index = int(input("Livro: "))
        usuario.devolver_livro(usuario.livros_emprestados[livro_index])

    elif op == "5":
        biblioteca.listar_livros_disponiveis()

    elif op == "6":
        biblioteca.listar_livros_emprestados()

    elif op == "7":
        break






        