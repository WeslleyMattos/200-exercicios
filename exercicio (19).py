# Elaborar um algoritmo que lê 3 valores a,b,c e os escreve. A seguir, encontre o maior dos 3 valores e o escreva com a mensagem : "É o maior ". a + b + | a - b |Maior de a e b =

a = float(input('Digite o valor A: '))
b = float(input('Digite o valor B: '))
c = float(input('Digite o valor C: '))

print(f'Os valores digitados sao: {a}, {b}, {c}')

maior = max(a, b, c)
print (f'O maior é: {maior}')