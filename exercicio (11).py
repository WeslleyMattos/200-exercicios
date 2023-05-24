#Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer no plano, P(x1,y1) e P(x2,y2), escreva a distância entre eles. A fórmula que efetua tal cálculo é
#d = raiz quadrada de (x1 - x2 )² + (y1 - y2)²
import math

x1 = float(input('Digite valor do x1: '))
x2 = float(input('Digite valor do x2: '))
y1 = float(input('Digite valor do y1: '))
y2 = float(input('Digite valor do y2: '))

distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f'A distancia entre os pontos P(x1,y1) e P(x2,y2) é {distancia:.2f}.')