class Livros:
    def __init__(self):
        self.livros = []

    def mostrar_livros(self): 
        print(f"{self.livros}")

    def cadastrar_livros (self,titulo,autor,ano): 
        livro = {'titulo':titulo ,'autor':autor,'ano':ano , 'status': "Disponivel"}        
        self.livros.append(livro)


    def verificador_de_estoque(self,titulo):

        titulo = titulo.strip().lower()
        for livro in self.livros:
            if livro['titulo'].strip().lower()== titulo:
                if livro['status'].strip().lower() == "Disponivel":
                    print(f"O Livros {}")
                return
        print("Não Tem") 

    def emprestar_livros (self):


        print(f"O Leitor solicitou o emprestimo do livro...{self.livros}")


class Leitor:
    def __init__(self,nome):
        self.nome = nome
        self.cadastrados = []


    def cadastrar_leitor(self):
        leitor = {self.nome}
        self.cadastrados.append(leitor)

    def mostrar_leitores_cadastrados(self): 
          print(f"{self.cadastrados}")





#Parte da execução

livros = Livros()
livros.cadastrar_livros("Turma da Monica", "Mauricio de Souza", 1990)
livros.verificador_de_estoque("Turma da Monica")


#Pessoa = Leitor("Pedrinho BH")
#Pessoa.cadastrar_leitor()
#Pessoa.mostrar_leitores_cadastrados()




