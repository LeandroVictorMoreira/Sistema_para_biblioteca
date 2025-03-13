from biblioteca import Livros, Leitor, Emprestimo

#Criando instâncias
livros =Livros()
leitor =Leitor()
emprestimo = Emprestimo(livros)




#Cadastro de Leitor
leitor.cadastrar_leitor("PedrinhoBH")

#Cadastro de Livros, incluindo titulo, autor e ano de Lançamento
livros.cadastrar_livros("Turma da Monica", "Mauricio de Souza", 1990)

#Realizando emprestimo de Livros, informando titulo, nome do leitor e chamando instancias
emprestimo.emprestar_livros("Turma da Monica","PedrinhoBH",leitor,livros)#




 