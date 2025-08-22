meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data = input("Digite uma data de nascimento (dd/mm/aaaa): ")
dia, mes, ano = data.split('/')
mes_extenso = meses[int(mes)-1]

print(f"Você nasceu em {int(dia)} de {mes_extenso} de {ano}.")
