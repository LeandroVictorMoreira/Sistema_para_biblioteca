class Livros: #Classe Livros 
    def __init__(self):
        self.livros = []

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

 

    def emprestar_livros (self,titulo,nome,leitor):

        cadastro_leitor = leitor.verifica_cadastro(nome) #chamada da função para verificar se está cadastrado
        retorno = self.verificador_de_estoque(titulo)
        if cadastro_leitor == False:
            print("Leitor não cadastrado, gentileza primeiro realizar o cadastro!")
        for livro in self.livros:
            if retorno == True and cadastro_leitor == True:
                print(f"O Livro {livro['titulo']} está sendo emprestado para {nome}.")
                livro['status'] = 'emprestado'
                leitor.associar_livro_ao_leitor(nome,titulo)
                return
            
        print("Infelizmente esse titulo não está disponivel para emprestimo")


    def devolver_livros(self,titulo):
        retorno =self.verificador_de_estoque(titulo)
        for livro in self.livros:
            if retorno == False:
                print(f"O livro {livro['titulo']} atualmente emprestado para {leitor['nome']}")  
                livro['status'] = 'disponivel'



class Leitor:
    def __init__(self):
        self.leitores_cadastrados = []


    def cadastrar_leitor(self,nome):
        leitor = {'nome':nome}
        self.leitores_cadastrados.append(leitor)

    def mostrar_leitores_cadastrados(self): 
          print(f"{self.cadastrados}")

    def verifica_cadastro(self,nome):
        nome = nome.strip().lower() #Retira os espaços e deixa em minusculo
        for leitor in self.leitores_cadastrados:
            if leitor['nome'].strip().lower()== nome.lower():
                print("Leitor cadastrado!")
                return True
        return False

    def associar_livro_ao_leitor(self,nome,titulo): # Função quefaz vinculo do nome do livro ao leitor que está com ele no momento
        nome = nome.strip().lower()

        for leitor in self.leitores_cadastrados:
            if leitor['nome'].strip().lower() == nome:
                if 'livros_em_emprestimo' not in leitor:
                    leitor['livros_em_emprestimo'] = []
                leitor['livros_em_emprestimo'].append(titulo)
                print(self.leitores_cadastrados)



#Parte da execução

livros =Livros()
leitor =Leitor()
leitor.cadastrar_leitor("PedrinhoBH")
livros.cadastrar_livros("Turma da Monica", "Mauricio de Souza", 1990)
livros.emprestar_livros("Turma da Monica","PedrinhoBH",leitor)
#livros.devolver_livros("Turma da Monica")

#Pessoa = Leitor("Pedrinho BH")
#Pessoa.cadastrar_leitor()
#Pessoa.mostrar_leitores_cadastrados()




