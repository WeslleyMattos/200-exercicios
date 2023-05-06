# Escrever um algoritmo que lê a hora de início de um jogo e a hora do final do jogo (considerando apenas horas inteiras) e calcula e mostra a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte. 

print("Determine as horas de um jogo para ver a duração total, apenas horas inteiras!")

inicio = int(input("Digite a hora de início do jogo: "))
final = int(input("Digite a hora do final do jogo: "))

if inicio < final:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final  

print(f"A duração do jogo foi de {duracao} horas.")
