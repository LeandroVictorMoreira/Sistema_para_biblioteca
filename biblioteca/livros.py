
class Livros: #Classe Livros 
    def __init__(self):
        self.livros = []
        self.livros_emprestados = []

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

 

   
         

    