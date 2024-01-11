from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def emprestarLivro(id: int):
    livro = buscarLivro(id)
    if not livro: #Se o livro não existe
        print('Erro: Livro não encontrado!')
        return
    if not livro['disponivel']: #Se o livro não está disponível (if not True)
        print('Erro: O livro está indisponível')
        return
    livro['disponivel'] = False
    print('Empréstimo realizado com sucesso!')

def devolverLivro(id: int):
    livro = buscarLivro(id)
    if not livro: #Se o livro não existe
        print('Erro: Livro não encontrado!')
        return
    if livro['disponivel']: #Se o livro está disponível (if True)
        print('Erro: O livro já está disponível')
        return
    livro['disponivel'] = True
    print('Devolução realizada com sucesso!')


if __name__ == '__main__':
    print(livros)
    devolverLivro(1)
    print(livros)