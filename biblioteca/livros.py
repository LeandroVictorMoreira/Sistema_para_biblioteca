from .emprestimo import Emprestimo

class Livros: #Classe Livros 
    def __init__(self):
        self.livros = []
        self.livros_emprestados = []
        self.emprestimo = Emprestimo()

    def mostrar_livros(self): 
        print(f"{self.livros}")

    def cadastrar_livros (self,titulo,autor,ano):  #Função para cadastrar os livros na lista "livros=[]"
        livro = {'titulo':titulo ,'autor':autor,'ano':ano , 'status': "disponivel"}        
        self.livros.append(livro) #Append faz a adição do livro na lista


    def verificador_de_estoque(self,titulo):

        titulo = titulo.strip().lower() #Retira os espaços e deixa em minusculo
        for livro in self.livros:       #Procura o titulo mencionado na lista livros
            if livro['titulo'].strip().lower()== titulo: #Comparação
                if livro['status'].strip().lower() == "disponivel":
                    print(f"O Livro {livro['titulo']} está {livro['status']}")
                    return True

        return False 

 

    def emprestar_livros (self,titulo,nome,leitor,livros):

        cadastro_leitor = leitor.verifica_cadastro(nome) #chamada da função para verificar se está cadastrado
        retorno = self.verificador_de_estoque(titulo)
        if cadastro_leitor == False:
            print("Leitor não cadastrado, gentileza primeiro realizar o cadastro!")
        for livro in self.livros:
            if retorno == True and cadastro_leitor == True:
                print(f"O Livro {livro['titulo']} está sendo emprestado para {nome}.")
                livro['status'] = 'emprestado'
                self.emprestimo.associar_leitor_ao_livro(nome,titulo)
                return

        print("Infelizmente esse titulo não está disponivel para emprestimo")
         

    