n = int (input("Digite o núemro de respondentes:"))
soma=0
x = n 

while n > 0:
    id=int(input("Qual a sua idade:"))
    soma= soma + id
    n = n - 1 

media = soma / x
print (f"A media das idades é: {media:.2f}")
