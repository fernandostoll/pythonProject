class livro
    def __init__(self, titulo, autor, num_paginas, isbn):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        self.isbn = isbn

    def exibir_informacoes(self):
        return f'titulo: {self.titulo}\nAutor: {self.autor}\nNumero de paginas: {self.num_paginas}\nIsbn: {self.isbn}'

livro = livro('aventuras de sherlock Homes', 'arthur Conan Doyle', 250, '978-3-16-148410-0')
informacoes_livro = livro1.exibir_informacoes
print(informacoes_livro)