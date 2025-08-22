frase = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
indices = [i for i, c in enumerate(frase) if c in vogais]
print(f"{len(indices)} vogais")
print("Índices", indices)
