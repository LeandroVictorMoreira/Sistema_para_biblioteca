from biblioteca import Livros
class Emprestimo:
    def __init__(self,livros):
        self.livros = livros 
        self.livros_emprestados = []
    
    def devolver_livros(self,titulo):
        retorno =self.verificador_de_estoque(titulo)
        for livro in self.livros:
            if retorno == False:
                print(f"O livro {livro['titulo']} atualmente emprestado para {leitor['nome']}")  
                livro['status'] = 'disponivel'

    def associar_leitor_ao_livro(self,nome,titulo,livros):
        titulo = titulo.strip().lower()

        for livro in self.livros.livros:
            if livro['titulo'].strip().lower() == titulo:
                if 'emprestado_a' not in livro:
                    livro['emprestado_a'] = []
                livro['emprestado_a'].append(nome)
            self.livros_emprestados.append(livro)
            self.mostrar_livros_emprestados()


    def mostrar_livros_emprestados(self):
        print(self.livros_emprestados)


    def emprestar_livros (self,titulo,nome,leitor,livros):

        cadastro_leitor = leitor.verifica_cadastro(nome) #chamada da função para verificar se está cadastrado
        retorno = livros.verificador_de_estoque(titulo)
        if cadastro_leitor == False:
            print("Leitor não cadastrado, gentileza primeiro realizar o cadastro!")
        for livro in self.livros.livros:
            if retorno == True and cadastro_leitor == True:
                print(f"O Livro {livro['titulo']} está sendo emprestado para {nome}.")
                livro['status'] = 'emprestado'
                self.associar_leitor_ao_livro(nome,titulo,livros)
                return

        print("Infelizmente esse titulo não está disponivel para emprestimo")ddd