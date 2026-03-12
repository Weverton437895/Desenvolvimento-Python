class Livro:

    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True
    
    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        else:
            print("Livro já está emprestado")
            return False

    def devolver(self):
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return (f"{self.titulo} - {self.autor} {self.ano} | {status} ")

    
class LivroDigital(Livro):
          def __init__(self, titulo, autor, ano, tamanho_arquivo):
            super().__init__(titulo, autor, ano)
            self.tamanho_arquivo = tamanho_arquivo

          def __str__(self):
            status = "Disponível" if self.disponivel else "Emprestado"
            return f"{self.titulo} - {self.autor} ({self.ano}) | {status} | {self.tamanho_arquivo}MB"


