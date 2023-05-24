#24	Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo. 

numero = int(input('Digite um número inteiro: '))
resultado = numero % 2 #qualquer resto da divisao de numero par vai ser igual a 0, e impar igual 1 se fizer por 2
if resultado == 0:
    print('O número escolhido é PAR!')
else:
    print('O número escolhido é IMPAR!')