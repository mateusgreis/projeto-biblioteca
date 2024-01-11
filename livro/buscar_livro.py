from livro.livro_repositorio import livros

def buscarLivro(id: int) -> dict or None: #Ou retorna um dicionário ou não retorna nada / A setinha indica o que a função irá retornar
    for livro in livros:
        if livro['id'] == id: #Se o id que eu tenho na lista é igual ao id que o usuário informou
            return livro
    return None
    # Não preciso informar return None pq por padrão ele ja retorna none se não encontrar

if __name__ == '__main__':
    print(buscarLivro(1))
    print(buscarLivro(2))