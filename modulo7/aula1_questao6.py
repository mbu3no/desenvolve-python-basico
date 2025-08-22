frase = input("Digite uma frase: ")
palavra = input("Digite a palavra objetivo: ").lower()
palavras = frase.replace('.', '').replace(',', '').split()
anagramas = [p for p in palavras if sorted(p.lower()) == sorted(palavra)]
print("Anagramas:", anagramas)
