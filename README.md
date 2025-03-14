
# Sistema de Biblioteca


O Projeto é um sistema para gerenciamento de biblioteca, feito em python ele foi projetado para o cadastro de livros e leitores, realização de emprestimos e devoluções de livros.



## Funcionalidades

- Cadastro de livros: Adiciona livros à biblioteca com título, autor e ano de publicação.

- Cadastro de leitores: Permite o cadastro de leitores que podem pegar livros emprestados.

- Empréstimos: Permite emprestar livros para leitores registrados, garantindo que o livro não esteja emprestado a outra pessoa.

- Devoluções: Permite devolver livros à biblioteca, atualizando seu status para "disponível" para bloquear novos emprestimos.

- Listagem de livros: Exibe todos os livros cadastrados, mostrando seu status (disponível ou emprestado).



## estrutura

- main.py - Arquivo principal que chama as funções.
biblioteca/

- init.py - Torna a pasta 'biblioteca' um pacote.

- livros.py - Lógica de manipulação de livros (cadastro, status e listagem).

- leitores.py - Lógica de manipulação de leitores (cadastro e verificação).

- emprestimos.py - Lógica de empréstimos de livros (realização e devolução).

- db.py - Lógica de conexão com o banco de dados (se houver necessidade).




## Demonstração

# Cadastro de leitores
leitor1 = Leitor("João")
leitor_manager.cadastrar_leitor(leitor1)

# Cadastro de livros
livro1 = Livro("O Alquimista", "Paulo Coelho", 1988)
livro_manager.cadastrar_livro(livro1)

# Realizando empréstimo
emprestimo_manager.realizar_emprestimo(livro1, leitor1)

# Devolvendo livro
emprestimo_manager.devolver_livro(livro1, leitor1)

# Banco de Dados

A integração é realizada junto a criação do banco de dados nomeado pessoas