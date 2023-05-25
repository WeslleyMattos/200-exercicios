#30	Escrever um algoritmo que lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo [10,20] e quantos deles estão fora deste intervalo, mostrando estas informações.

dentro = 0
fora = 0
lista = []

for i in range(1,11):
    valor = float(input(f'Digite o {i}° valor: '))
    lista.append([valor])

for valor in lista:
    if valor[0] >= 10 and valor[0] <= 20:
        dentro += 1
    else:
        fora += 1

print("Valores dentro do intervalo [10, 20]:", dentro)
print("Valores fora do intervalo [10, 20]:", fora)
