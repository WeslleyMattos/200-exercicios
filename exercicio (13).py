#13	 Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e mostre-a expressa apenas em dias. 

from datetime import date

print('Informe sua data de nascimento: ')
dia = int(input("Dia:  "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data_atual = date.today()

data_nascimento = date(ano, mes, dia) #aqui tem q ser assim pq é como é as datas nos EUA

diferenca = data_atual - data_nascimento

idade_dias = diferenca.days

print(f"A idade é de {idade_dias} dias.")

#link de estudo: https://www.youtube.com/watch?v=A7S_RwWcrK0&ab_channel=HashtagPrograma%C3%A7%C3%A3o