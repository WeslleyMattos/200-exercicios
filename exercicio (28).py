#28	Escrever um algoritmo que lê 50 valores, um de cada vez, e encontra e mostra o maior deles

maior = 0
for i in range(1,51):
    valor = float(input(f'Digite o {i}° valor: '))
    maior = max(maior, valor)
print(f'O maior valor digitado foi: {maior}.')