genero = input("Digite seu gênero (M ou F): ").upper()
idade = int(input("Digite sua idade: "))
tempo_servico = int(input("Digite seu tempo de serviço (anos): "))

aposentar = (genero == "F" and idade > 60) or (genero == "M" and idade > 65) or (tempo_servico >= 30) or (idade >= 60 and tempo_servico >= 25)
print(aposentar)
