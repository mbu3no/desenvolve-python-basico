import re

with open("estomago.txt", "r", encoding="utf-8") as f:
    linhas = f.readlines()

print("Primeiras 25 linhas:")
print(''.join(linhas[:25]))

print("Número de linhas:", len(linhas))

linha_maior = max(linhas, key=lambda x: len(x))
print("Linha com mais caracteres:", linha_maior.strip())

texto = ''.join(linhas).lower()
nonato_count = len(re.findall(r"\bnonato\b", texto))
iria_count = len(re.findall(r"\bíria\b", texto))
print("Menções a Nonato:", nonato_count)
print("Menções a Íria:", iria_count)
