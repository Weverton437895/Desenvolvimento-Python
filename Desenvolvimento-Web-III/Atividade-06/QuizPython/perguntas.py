class Perguntas:
    
    perguntas = [
        {"enunciado": "1. Qual comando exibe algo na tela?",
         "alternativas": ["A) input()", "B) print()", "C) echo()"],
         "resposta": "B"},

        {"enunciado": "2. Qual função lê dados do usuário?",
         "alternativas": ["A) read()", "B) input()", "C) scan()", "D) get()"],
         "resposta": "B"},

        {"enunciado": "3. O que o código abaixo faz?\nnome = input(\"Digite seu nome: \")\nprint(nome)",
         "alternativas": ["A) Ignora o usuário", "B) Mostra sempre \"nome\"", "C) Lê e exibe o que o usuário digitou", "D) Dá erro"],
         "resposta": "C"},

        {"enunciado": "4. Qual será o tipo da variável?\nx = \"10\"",
         "alternativas": ["A) int", "B) float", "C) str", "D) bool"],
         "resposta": "C"},

        {"enunciado": "5. Qual será o resultado?\nx = int(\"5\")\nprint(x + 2)",
         "alternativas": ["A) 52", "B) 7", "C) erro", "D) \"7\""],
         "resposta": "B"},

        {"enunciado": "6. O que esse código imprime?\nx = \"5\"\nif x == 5:\n    print(\"A\")\nelse:\n    print(\"B\")",
         "alternativas": ["A) A", "B) B", "C) 3", "D) Erro"],
         "resposta": "B"},

        {"enunciado": "7. Complete corretamente:\nif x ___ 10:\n    print(\"Diferente\")",
         "alternativas": ["A) =", "B) ==", "C) :=", "D) !="],
         "resposta": "D"},

        {"enunciado": "8. Qual será a saída?\nfor i in range(3):\n    print(i)",
         "alternativas": ["A) 1 2 3", "B) 0 1 2", "C) 0 1 2 3", "D) Erro"],
         "resposta": "B"},

        {"enunciado": "9. O que esse código faz?\ni = 0\nwhile i < 3:\n    print(i)\n    i += 1",
         "alternativas": ["A) Imprime 1,2,3", "B) Loop infinito", "C) Imprime 0,1,2", "D) Erro"],
         "resposta": "C"},

        {"enunciado": "10. Palavra-chave para criar função:",
         "alternativas": ["A) func", "B) def", "C) function", "D) lambda"],
         "resposta": "B"},

        {"enunciado": "11. O que será exibido?\ndef add(a, b):\n    return a + b\nprint(add(2, 3))",
         "alternativas": ["A) 23", "B) 5", "C) erro", "D) None"],
         "resposta": "B"},

        {"enunciado": "12. Para que servem funções?",
         "alternativas": ["A) Repetir código", "B) Organizar e reutilizar código", "C) Criar listas", "D) Encerrar programa"],
         "resposta": "B"},

        {"enunciado": "13. O que é um parâmetro?",
         "alternativas": ["A) Retorno", "B) Valor passado para função", "C) Variável global", "D) Classe"],
         "resposta": "B"},

        {"enunciado": "14. O que falta para funcionar?\ndef teste():\n    print(\"OK\")\n____",
         "alternativas": ["A) print()", "B) return", "C) teste()", "D) input()"],
         "resposta": "C"},

        {"enunciado": "15. Como criar uma lista?",
         "alternativas": ["A) {}", "B) []", "C) ()", "D) <>"],
         "resposta": "B"},

        {"enunciado": "16. Qual será a saída?\nlista = [10, 20, 30]\nprint(lista[-1])",
         "alternativas": ["A) 0", "B) 30", "C) 20", "D) Erro"],
         "resposta": "B"},

        {"enunciado": "17. Como acessar o primeiro elemento?",
         "alternativas": ["A) lista[1]", "B) lista[0]", "C) lista[-1]", "D) lista.first()"],
         "resposta": "B"},

        {"enunciado": "18. O que esse código faz?\nlista = []\nlista.append(5)",
         "alternativas": ["A) Remove valor", "B) Adiciona 5", "C) Substitui lista", "D) Dá erro"],
         "resposta": "B"},

        {"enunciado": "19. O que é um dicionário?",
         "alternativas": ["A) Lista", "B) Chave e valor", "C) Número", "D) Texto"],
         "resposta": "B"},

        {"enunciado": "20. Qual será a saída?\npessoa = {\"nome\": \"Ana\"}\nprint(pessoa[\"nome\"])",
         "alternativas": ["A) nome", "B) Ana", "C) Erro", "D) None"],
         "resposta": "B"},

        {"enunciado": "21. Como acessar um valor no dicionário?",
         "alternativas": ["A) dict[0]", "B) dict.chave", "C) dict[\"chave\"]", "D) dict()"],
         "resposta": "C"},

        {"enunciado": "22. O que esse código faz?\naluno = {}\naluno[\"nome\"] = \"Carlos\"",
         "alternativas": ["A) Remove item", "B) Cria lista", "C) Adiciona chave e valor", "D) Dá erro"],
         "resposta": "C"},

        {"enunciado": "23. Como criar um dicionário corretamente?",
         "alternativas": ["A) [\"nome\", \"João\"]", "B) (\"nome\", \"João\")", "C) {\"nome\": \"João\"}", "D) nome = João"],
         "resposta": "C"},

        {"enunciado": "24. O que é uma classe?",
         "alternativas": ["A) Função", "B) Molde para objetos", "C) Variável", "D) Lista"],
         "resposta": "B"},

        {"enunciado": "25. Complete:\n_____ Pessoa:\n    pass",
         "alternativas": ["A) def", "B) class", "C) func", "D) create"],
         "resposta": "B"},

        {"enunciado": "26. O que é um objeto?",
         "alternativas": ["A) Classe", "B) Instância de classe", "C) Função", "D) Loop"],
         "resposta": "B"},

        {"enunciado": "27. O que esse código faz?\nclass Pessoa:\n    pass\np = Pessoa()",
         "alternativas": ["A) Cria função", "B) Cria objeto", "C) Dá erro", "D) Cria lista"],
         "resposta": "B"},

        {"enunciado": "28. Complete o construtor:\nclass Pessoa:\n    def ______(self, nome):\n        self.nome = nome",
         "alternativas": ["A) init", "B) __init__", "C) start", "D) create"],
         "resposta": "B"},

        {"enunciado": "29. Qual será a saída?\nclass Pessoa:\n    def __init__(self, nome):\n        self.nome = nome\np = Pessoa(\"Ana\")\nprint(p.nome)",
         "alternativas": ["A) nome", "B) Ana", "C) Pessoa", "D) Erro"],
         "resposta": "B"},

        {"enunciado": "30. O que é self?",
         "alternativas": ["A) Variável global", "B) Referência ao objeto", "C) Função", "D) Loop"],
         "resposta": "B"},

        {"enunciado": "31. O que é um atributo?",
         "alternativas": ["A) Função", "B) Característica do objeto", "C) Loop", "D) Classe"],
         "resposta": "B"},

        {"enunciado": "32. O que é um método?",
         "alternativas": ["A) Variável", "B) Função dentro da classe", "C) Lista", "D) Tipo"],
         "resposta": "B"},

        {"enunciado": "33. O que esse código representa?\nclass Animal:\n    pass\nclass Cachorro(Animal):\n    pass",
         "alternativas": ["A) Lista", "B) Função", "C) Herança", "D) Condição"],
         "resposta": "C"},

        {"enunciado": "34. O que está errado?\nclass Pessoa:\n    def init(self):\n        pass",
         "alternativas": ["A) Falta class", "B) Falta self", "C) Falta __ no init", "D) Nada"],
         "resposta": "C"},

        {"enunciado": "35. Em Python, qual é a função da identação no código?",
         "alternativas": ["A) Melhorar apenas a estética do código, sem impacto na execução",
                          "B) Definir blocos de código, como estruturas de controle e funções",
                          "C) Substituir o uso de comentários no código",
                          "D) Indicar ao interpretador quais bibliotecas devem ser importadas"],
         "resposta": "B"}
    ]