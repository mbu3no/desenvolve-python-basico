frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
frase_modificada = ''.join(['*' if c in vogais else c for c in frase])
print("Frase modificada:", frase_modificada)
