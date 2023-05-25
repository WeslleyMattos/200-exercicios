#27	Escrever um algoritmo que lê 5 valores, um de cada vez, e conta quantos destes valores são negativos, mostrando esta informação.
negativos = 0
for i in range(1,6):
    valores = float(input(f'Digite o {i}° valor: '))
    if valores < 0:
        negativos += 1
print(f'O total de valores negativos foi de: {negativos}')