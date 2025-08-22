import random

def encrypt(nomes):
    n = random.randint(1, 10)
    criptografados = []
    for nome in nomes:
        novo = ''
        for c in nome:
            codigo = ord(c)
            codigo_novo = (codigo - 33 + n) % (126 - 33 + 1) + 33
            novo += chr(codigo_novo)
        criptografados.append(novo)
    return criptografados, n

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave = encrypt(nomes)
print("Chave:", chave)
print("Nomes criptografados:", nomes_cript)
