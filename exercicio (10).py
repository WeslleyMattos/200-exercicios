#10	Escrever um algoritmo que lê a hora de início de um jogo e a hora de término do jogo, ambas subdivididas em 2 valores distintos, a saber: horas e minutos. Calcular e escrever a duração do jogo, também em horas e minutos, considerando que o tempo máximo de duração de um jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

hora_inicio = int(input("hora inicio: "))
minuto_inicio = int(input("minuto inicio: "))

termino = int(input("término do jogo (horas): "))
min_termino = int(input("término do jogo (minutos): "))

duracao_horas = termino - hora_inicio
duracao_minutos = min_termino - minuto_inicio

if duracao_horas < 0:
    duracao_horas += 24

if duracao_minutos < 0:
    duracao_minutos += 60
    duracao_horas -= 1

print(f"A duração do jogo foi de {duracao_horas} horas e {duracao_minutos} minutos.")
