distancia = float(input("Digite a distância da entrega (km): "))
peso = float(input("Digite o peso do pacote (kg): "))

if distancia <= 100:
    valor_kg = 1
elif distancia <= 300:
    valor_kg = 1.5
else:
    valor_kg = 2

frete = valor_kg * peso

if peso > 10:
    frete += 10

print("Valor do frete: R${:.2f}".format(frete))
