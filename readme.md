Sistema de Biblioteca


O Projeto é um sistema para gerenciamento de biblioteca, feito em python ele foi projetado para o cadastro de livros e leitores, realização de emprestimos e devoluções de livros.


Funcionalidades
Cadastro de livros: Adiciona livros à biblioteca com título, autor e ano de publicação.
Cadastro de leitores: Permite o cadastro de leitores que podem pegar livros emprestados.
Empréstimos: Permite emprestar livros para leitores registrados, garantindo que o livro não esteja emprestado a outra pessoa.
Devoluções: Permite devolver livros à biblioteca, atualizando seu status para "disponível".
Listagem de livros: Exibe todos os livros cadastrados, mostrando seu status (disponível ou emprestado).
Estrutura do Projeto
bash
Copiar
Editar
biblioteca/
│
├── main.py             # Arquivo principal que chama as funções
├── biblioteca/
│   ├── __init__.py     # Torna a pasta 'biblioteca' um pacote
│   ├── livros.py       # Lógica de manipulação de livros
│   ├── leitores.py     # Lógica de manipulação de leitores
│   └── emprestimos.py  # Lógica de empréstimos
├── db.py              # Lógica de conexão com o banco de dados
└── requirements.txt    # Arquivo para dependências (se necessário)