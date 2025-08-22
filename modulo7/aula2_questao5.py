import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) <= 3:
            return palavra
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]
    
    palavras = frase.split()
    return ' '.join(embaralhar_palavra(p) for p in palavras)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
