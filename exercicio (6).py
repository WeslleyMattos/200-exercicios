# Escreva um algoritmo para ler o número de voltas dadas, a extensão do circuito, em metros, e o tempo de duração, em minutos, de uma corrida de Fórmula um. Depois disto, calcular e mostrar a velocidade média do primeiro colocado, em Km/h. 

voltas = int(input('Escreva o número de voltas dadas: '))
extensao = float(input('Agora escreva a extensão do circuito em metros: '))
tempo = float(input('Agora escreva o tempo de duração em minutos: '))

tempo_hora = tempo / 60

velocidade = ((voltas * extensao) / tempo_hora / 1000)

print(f'A velocidade média do primeiro colocado é de {velocidade}Km/h')
