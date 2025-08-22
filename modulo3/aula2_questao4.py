classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ").lower()
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))

if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = 5 < forca <= 15 and 5 < magia <= 15
else:
    valido = False

print("Pontos de atributo consistentes com a classe escolhida:", valido)
