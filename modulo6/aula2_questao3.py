import random

lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(list(set(lista1) & set(lista2)))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção:", interseccao)

for elem in interseccao:
    print(f"{elem}: (lista1={lista1.count(elem)}, lista2={lista2.count(elem)})")
