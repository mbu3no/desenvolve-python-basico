cpf = input("Digite o CPF (XXX.XXX.XXX-XX): ")

numeros = [int(d) for d in cpf if d.isdigit()]

# Calcula 1º dígito
soma = sum([numeros[i] * (10 - i) for i in range(9)])
resto = soma % 11
dig1 = 0 if resto < 2 else 11 - resto

# Calcula 2º dígito
soma = sum([numeros[i] * (11 - i) for i in range(9)]) + dig1 * 2
resto = soma % 11
dig2 = 0 if resto < 2 else 11 - resto

if dig1 == numeros[9] and dig2 == numeros[10]:
    print("Válido")
else:
    print("Inválido")
