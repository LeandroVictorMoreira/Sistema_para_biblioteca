class Emprestimo:
    
    def devolver_livros(self,titulo):
        retorno =self.verificador_de_estoque(titulo)
        for livro in self.livros:
            if retorno == False:
                print(f"O livro {livro['titulo']} atualmente emprestado para {leitor['nome']}")  
                livro['status'] = 'disponivel'

    def associar_leitor_ao_livro(self,nome,titulo):
        titulo = titulo.strip().lower()

        for livro in self.livros:
            if livro['titulo'].strip().lower() == titulo:
                if 'emprestado_a' not in livro:
                    livro['emprestado_a'] = []
                livro['emprestado_a'].append(nome)
        self.livros_emprestados.append(livro)
        self.mostrar_livros_emprestados()


    def mostrar_livros_emprestados(self):
        print(self.livros_emprestados)