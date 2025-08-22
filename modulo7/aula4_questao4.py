import random

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f if linha.strip()]

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    enforcado_stages = f.read().split("\n\n")

palavra = random.choice(palavras).upper()
progresso = ["_" for _ in palavra]
erros = 0
max_erros = 6
letras_chutadas = []

def imprime_enforcado(erros):
    print(enforcado_stages[erros])

while erros < max_erros and "_" in progresso:
    print("Palavra:", ' '.join(progresso))
    letra = input("Digite uma letra: ").upper()
    
    if letra in letras_chutadas:
        print("Você já tentou essa letra.")
        continue
    letras_chutadas.append(letra)
    
    if letra in palavra:
        for i, l in enumerate(palavra):
            if l == letra:
                progresso[i] = letra
    else:
        erros += 1
        imprime_enforcado(erros)

if "_" not in progresso:
    print("Parabéns! Você ganhou:", palavra)
else:
    print("Você perdeu! Palavra era:", palavra)
