import random

num_elementos = random.randint(5, 20)
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

print("Lista elementos:", elementos)
print("Soma dos valores:", sum(elementos))
print("Média dos valores:", sum(elementos)/len(elementos))
