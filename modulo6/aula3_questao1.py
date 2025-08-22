numeros = []
while len(numeros) < 4 or input("Deseja continuar? (s/n): ").lower() == 's':
    numeros.append(int(input("Digite um número inteiro: ")))

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Elementos de índice par:", numeros[::2])
print("Elementos de índice ímpar:", numeros[1::2])
