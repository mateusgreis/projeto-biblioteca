from livro.livro_repositorio import livros
from livro.buscar_livro import buscarLivro

def deletarLivro(id: int):
    livro = buscarLivro(id) #Aproveitar a função de buscar, e buscar o id informado pelo usuário
    if livro: #Se existir o livro (encontrar id)
        livros.remove(livro) #Busca na lista qual item tem aquele valor e deleta ele
        print('Livro removido com sucesso!')
    else:
        print('Erro: Livro não encontrado!')

if __name__ == '__main__':
    print(livros)
    deletarLivro(1)
    print(livros)
    deletarLivro(1)
