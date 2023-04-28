#Escreva um algoritmo que leia 3 números inteiros e mostre o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num2 > num1:
    num1 = num2
if num3 > num1:
    num1 = num3

print("O maior número é:", num1)

#Link de estudo: https://www.youtube.com/watch?v=K10u3XIf1-Q&t=1527s&ab_channel=CursoemV%C3%ADdeo