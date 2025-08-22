livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1216],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["Grande Sertão: Veredas", "João Guimarães Rosa", 1956, 624],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["Cem Anos de Solidão", "Gabriel Garcia Marquez", 1967, 417]
]

with open("meus_livros.csv", "w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(','.join(map(str, livro)) + "\n")
