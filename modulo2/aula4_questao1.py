comprimento = int(input("Digite o comprimento do terreno (m): "))
largura = int(input("Digite a largura do terreno (m): "))
preco_m2 = float(input("Digite o preço do metro quadrado: "))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print("O terreno possui {}m2 e custa R${:,.2f}".format(area_m2, preco_total))
