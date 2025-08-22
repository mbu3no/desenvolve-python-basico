pares = [x for x in range(20, 51) if x % 2 == 0]
print("Números pares entre 20 e 50:", pares)

quadrados = [x**2 for x in range(1, 10)]
print("Quadrados de 1 a 9:", quadrados)

div7 = [x for x in range(1, 101) if x % 7 == 0]
print("Números divisíveis por 7 de 1 a 100:", div7)

paridade = ["par" if x % 2 == 0 else "ímpar" for x in range(0, 30, 3)]
print("Paridade:", paridade)
