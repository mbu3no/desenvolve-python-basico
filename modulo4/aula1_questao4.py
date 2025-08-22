n = int(input("Digite N:"))
maior = 0

while n > 0:
    x = int(input("Digite x:"))
    if x > maior:
        maior = x
        n= n-1

    else:
        n=n-1

print(maior)
