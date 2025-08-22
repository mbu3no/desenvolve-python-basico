import string

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    frase_normalizada = ''.join(c.lower() for c in frase if c.isalnum())
    if frase_normalizada == frase_normalizada[::-1]:
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
