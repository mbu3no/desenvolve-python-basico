n1 = int(input("Digite a quantidade de elementos da lista 1: "))
lista1 = [int(input()) for _ in range(n1)]

n2 = int(input("Digite a quantidade de elementos da lista 2: "))
lista2 = [int(input()) for _ in range(n2)]

lista_intercalada = []
tamanho_min = min(n1, n2)

# Intercalando os elementos
for i in range(tamanho_min):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicionando elementos restantes da lista maior
if n1 > n2:
    lista_intercalada.extend(lista1[tamanho_min:])
elif n2 > n1:
    lista_intercalada.extend(lista2[tamanho_min:])

print("Lista intercalada:", *lista_intercalada)
