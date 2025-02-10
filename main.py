class Livros:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.livros = []



    def mostrar_livros(self): 
        pass
        print(f"{self.livros}")






    def cadastrar_livros (self): 
        livro = {self.titulo ,self.autor,self.ano}        
        self.livros.append(livro)





Teste = Livros("Turma da Monica", "Mauricio de Souza", 1990)

Teste.cadastrar_livros()
Teste.mostrar_livros()



