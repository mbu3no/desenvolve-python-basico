n= int(input("dIgite a quantidade de experimentos:"))
cont = 0
soma_sapo=0
soma_rato=0
soma_coelho=0

while cont < n:
    quantia = int(input())
    tipo=input()

    if tipo=='S':
        soma_sapo= soma_sapo + quantia 
    elif tipo=='R':
        soma_rato= soma_rato + quantia 
    elif tipo=='C':
        soma_coelho= soma_coelho + quantia 
    
    cont += 1

print("total de cobaias: ",soma_sapo + soma_rato + soma_coelho)
print("total de sapos: ",soma_sapo )
print("total de ratos: ",soma_rato )
print("total de coelhos: ",soma_coelho)
