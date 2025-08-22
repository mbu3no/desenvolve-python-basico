import random

numero = random.randint(1, 10)

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    if palpite < numero:
        print("Muito baixo, tente novamente!")
    elif palpite > numero:
        print("Muito alto, tente novamente!")
    else:
        print(f"Correto! O número é {numero}.")
        break
