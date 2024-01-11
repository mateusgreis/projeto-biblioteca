from livro.livro_repositorio import livros
from livro.registrar import registrarLivro
from livro.listar_livros import listarLivros
from livro.buscar_livro import buscarLivro
from livro.editar_livro import editarLivro
from livro.deletar_livro import deletarLivro

def menuBiblioteca():
    while True:
        print('--- MENU BIBLIOTECA ---')
        print('1 - Cadastrar livro')
        print('2 - Editar livro')
        print('3 - Remover livro')
        print('4 - Buscar livro')
        print('5 - Listar todos os livros')
        print('6 - Sair')
        opcao = int(input('Seleciona uma opção: '))
        # if 0 < opcao > 6:
        #     print('Erro: Opção inválida!')
        #     return
        if opcao == 0:
            print('Erro: Opção inválida!')
            return
        if opcao == 1:
            titulo = input('Digite o titulo do livro: ')
            editora = input('Digite a editora: ')
            registrarLivro(titulo, editora)
        elif opcao == 2:
            id = int(input('Informe o id do livro: '))
            titulo = input('Digite o titulo do livro: ')
            editora = input('Digite a editora: ')
            disponivel = input('Qual a disponibilidade?'
                               '1 - True / 2 - False')
            if disponivel == '1':
                editarLivro(id, titulo, editora, True)
            else:
                editarLivro(id, titulo, editora, False)
        elif opcao == 3:
            id = int(input('Informe o id do livro: '))
            deletarLivro(id)
        elif opcao == 4:
            id = int(input('Informe o id do livro: '))
            print(buscarLivro(id))
        elif opcao == 5:
            listarLivros()
        elif opcao == 6:
            break

if __name__ == '__main__':
    menuBiblioteca()

