class Biblioteca:
    
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        for livro in self.livros:
            if livro.disponivel:
                print(livro)

    def listar_livros_emprestados(self):
        for livro in self.livros:
            if not livro.disponivel:
                print(livro)