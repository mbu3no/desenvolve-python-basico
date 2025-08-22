frase = input("Digite uma frase: ")

vogais = sorted([c for c in frase if c.lower() in 'aeiou'])
consoantes = [c for c in frase if c.isalpha() and c.lower() not in 'aeiou']

print("Vogais:", vogais)
print("Consoantes:", consoantes)
