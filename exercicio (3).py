# Escrever um algoritmo que lê um conjunto de 4 valores e os mostre. A seguir, se o primeiro valor for 1, 
# mostrar os três valores seguintes em ordem crescente; se o primeiro valor for 2, mostrar os três valores 
# seguintes em ordem decrescente; se o primeiro valor for 3,
#  mostrar os três valores seguintes de forma que o maior valor entre os três fique entre os outros dois.
import os

print('Vamos começar escolhendo 4 valores entre 1 e 4:')
lista_valores = []
for valores in range (0,4):
    lista_valores.append(float(input(f'Digite o {valores+1}º valor: ')))

# verificando os valores
if lista_valores[0] == 1:
    crescente = sorted(lista_valores[1:])
    print('Valores em ordem crescente:', crescente)
elif lista_valores[0] == 2:
    decrescente = sorted(lista_valores[1:], reverse = True)
    print('Valores em ordem decrescente', decrescente)

elif lista_valores[0] == 3:
    meiuca = sorted(lista_valores[1:]) #meiuca → aquele fica no meio (fiquei sem criatividade pro nome dessa variavel)
    maior_valor = max(meiuca)
    meiuca.remove(maior_valor)
    meiuca.insert(1, maior_valor)
    print('O maior valor no meio', meiuca)
else:
    print('O primeiro valor não é válido! Tente novamente')


print('Aperte ENTER para limpar o terminal')
input()
os.system('cls')

#link de estudo: https://www.youtube.com/watch?v=cL4YDtFnCt4&t=1557s&ab_channel=CursoemV%C3%ADdeo
