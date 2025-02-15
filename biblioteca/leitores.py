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
                return Trued
        return False

    #def associar_livro_ao_leitor(self,nome,titulo): # Função que faz vinculo do nome do livro ao leitor que está com ele no momento
        nome = nome.strip().lower()

        for leitor in self.leitores_cadastrados:
            if leitor['nome'].strip().lower() == nome:
                if 'livros_em_emprestimo' not in leitor:
                    leitor['livros_em_emprestimo'] = []
                leitor['livros_em_emprestimo'].append(titulo)
                print(self.leitores_cadastrados)


