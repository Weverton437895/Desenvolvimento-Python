class Usuario:
    
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        if livro.emprestar():
            self.livros_emprestados.append(livro)
            print("Livro emprestado com sucesso.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
            print("Livro devolvido.")
        else:
            print("Este usuário não possui este livro.")

    def __str__(self):
        return f"{self.nome} - Matrícula: {self.matricula}"