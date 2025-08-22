import re

with open("frase.txt", "r", encoding="utf-8") as f:
    frase = f.read()

palavras = re.findall(r"[A-Za-zÀ-ÿ]+", frase)

with open("palavras.txt", "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
