import random

lista = [random.randint(-10, 10) for _ in range(20)]
print("Original:", lista)

maior_negativos = 0
inicio_del = 0
fim_del = 0
i = 0

while i < len(lista):
    if lista[i] < 0:
        j = i
        while j < len(lista) and lista[j] < 0:
            j += 1
        if (j - i) > maior_negativos:
            maior_negativos = j - i
            inicio_del = i
            fim_del = j
        i = j
    else:
        i += 1

if maior_negativos > 0:
    del lista[inicio_del:fim_del]

print("Editada:", lista)
