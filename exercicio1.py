#Escreva um algoritmo que lê 3 valores, a, b, c.
#Que calcula e mostra a média ponderada com pesos de 5 para o maior dos 3 valores e 2.5 para os outros 2
print('Calculando a média ponderada de três valores: ')
a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

if a >= b and a >= c:
    media = (5*a + 2.5*b + 2.5*c) / 10
elif b >= a and b >= c:
    media = (5*b + 2.5*a + 2.5*c) / 10
else:
    media = (5*c + 2.5*a + 2.5*b) / 10

print(f"A média ponderada com pesos é: {media:.2f}")

#LINK DE ESTUDO > https://www.youtube.com/watch?v=nRxl0WUplf4&ab_channel=DicasdematSandroCuri%C3%B3