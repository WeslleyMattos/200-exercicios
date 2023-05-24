#Faça um algoritmo que leia a idade de uma pessoa expressa em dias e mostre-a expressa em anos, meses e dias.

from datetime import datetime, timedelta #importando datetime dentro de datetime pra nao ficar repetindo codigo la embaixo

idade_em_dias = int(input('Use o script anterior pra saber uma idade em dias e digite ela aqui: '))

data_atual = datetime.now()
data_nascimento = data_atual - timedelta(days = idade_em_dias)

diferenca = data_atual - data_nascimento

anos = diferenca.days // 365 #usando // pra arredondar o resultado pra baixo de forma inteira
meses = (diferenca.days % 365) // 30 #aqui usando o resto da divisao de um ano dividindo por 30 q é a media dos meses
dias = (diferenca.days % 365) % 30 #aqui é o resto do resto, que da nos dias

print(f'A idade é de {anos} anos, {meses} meses e {dias} dias.')

#link estudo: https://www.youtube.com/watch?v=A7S_RwWcrK0&ab_channel=HashtagPrograma%C3%A7%C3%A3o