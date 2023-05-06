# O departamento que controla o índice de poluição do meio ambiente monitora três grupos de indústrias altamente poluidoras. 
# O índice de poluição aceitável varia de 0 a 0.25 miligramas de poluentes por metro cúbico de ar. 
# Se o índice sobe para 0.3 mg/m³ as indústrias do primeiro grupo são intimadas a suspender suas atividades, se o índice cresce para 0.4 mg/m³
# as do primeiro e segundo grupo são intimadas a suspender as atividades; e se o índice atingir 0.5 mg/m³, os três grupos devem paralisar as atividades. 
# Escrever um algoritmo que lê o índice de poluição medido e mostra a notificação na forma de uma frase 
# "grupo 1 deve parar" ou "grupos 1 e 2 devem parar" ou "os três grupos devem parar".
import os
from time import sleep

indice1 = 0.3
indice2 = 0.4
indice3 = 0.5

print('O departamento que controla o índice de poluição verificou que houve uma alteração no indice!')
print('Por favor escolha a opção em que o indice de poluição atual se encontra: ')
print('Digite A para indices de poluição em 0.3 \nDigite B para indices de poluição em 0.4 \nOu digite C para indices de poluição em 0.5')

escolha = str(input('>>>  '))
escolha = escolha.upper()

sleep (1)
print ('-=-' * 25)
print ('ANÁLISANDO...ANÁLISANDO...ANÁLISANDO...ANÁLISANDO...')
print ('-=-' * 25)
sleep (3)

if escolha == 'A':
    print('As indústrias do PRIMEIRO grupo estão sendo intimadas a suspender suas atividades imediatamente!')
elif escolha == 'B':
    print('As indústrias do PRIMEIRO e SEGUNDO grupo estão sendo intimadas a suspender as atividades imediatamente!')
elif escolha == 'C':
    print('OS TRÊS GRUPOS DEVEM SUSPENDER SUAS ATIVIDADES IMEDIATAMENTE!!!')
else:
    print('Opção inválida!')

input()
os.system('cls')

#Link de estudo: https://www.youtube.com/watch?v=B3F0IjH5WAM&t=326s&ab_channel=CursoemV%C3%ADdeo