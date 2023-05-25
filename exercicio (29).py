#29	Escrever um algoritmo que mostra todos os números ímpares entre 100 e 200. Dica: considere a existência de um operador "mod" cujo resultado é o resto da divisão de um número por outro.

for numero in range(100, 201):
    if numero % 2  != 0:
        print (numero)
