from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def editarLivro(id: int, titulo: str, editora: str, disponivel: bool):
    livro = buscarLivro(id)
    if livro: #Se existir o livro (se encontrar)
        livro['titulo'] = titulo
        livro['editora'] = editora
        livro['disponivel'] = disponivel
        print('Dados alterados com sucesso!')
        return #A boa prática recomenda usar assim, para ecitar muitos if e else
    print('Erro: Livro não encontrado!')

if __name__ == '__main__':
    print(livros)
    editarLivro(1,"Pedra Filosofal", "JK Editora", False)
    print(livros)