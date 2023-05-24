# Faça um algoritmo que leia o tempo de duração de um evento em uma fábrica expressa em segundos e mostre-o expresso em horas, minutos e segundos.

from datetime import datetime, timedelta

evento = int(input('Digite o tempo da duração do evento em SEGUNDOS!!: '))
evento =  timedelta(seconds = evento) #aqui transformando o valor digitado para segundos de verdade

horas = evento.seconds // 3600  #uma hora tem 3600 segundos entao divido o valor total pra pegar as horas arredondadas
minutos = (evento.seconds % 3600) // 60 #mesmo esquema, pegando o resto da divisao das horas dividindo por 60
segundos = evento.seconds % 60

print(f'A duração do evento foi de {horas} horas, {minutos} minutos e {segundos} segundos.')