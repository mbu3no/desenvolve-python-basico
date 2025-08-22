import random

valores = [random.randint(-100, 100) for _ in range(20)]

print("Lista ordenada:", sorted(valores))
print("Lista original:", valores)
print("Índice do maior valor:", valores.index(max(valores)))
print("Índice do menor valor:", valores.index(min(valores)))
