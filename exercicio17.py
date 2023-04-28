# #As tarifas do parkímetro para estacionamento nas ruas da cidade são: R$1,50 (30min), R$2,00 (1h), R$2,50 (1,5h) e R$3,00 (2h). 
# Faça um algoritmo que leia quantos R$ o motorista irá pagar (considere apenas estas quatro opções, sem troco), 
# calcule e escreva quantos minutos o seu veículo poderá ficar estacionado.
print('Nosso valores de estacinamento são: R$1,50 (30min), R$2,00 (1h), R$2,50 (1,5h) e R$3,00 (2h')
valor = (input("Digite o valor a ser pago para a conversão em minutos: "))
valor = valor.replace(',' , '.')
valor = float(valor)

if valor == 1.50:
    minutos = 30
elif valor == 2.00:
    minutos = 60
elif valor == 2.50:
    minutos = 90
elif valor == 3.00:
    minutos = 120
else:
    print("valor inválida!")
    minutos = None

if minutos != None:
    print("Seu veículo poderá ficar estacionado por", minutos, "minutos.")

#Link de estudo: https://www.youtube.com/watch?v=bIJK6f4ygGo&ab_channel=CFBCursos