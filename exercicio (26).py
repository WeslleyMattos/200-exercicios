# 26	Tendo como dados de entrada a altura e o sexo de uma pessoa (?M? masculino e ?F? feminino), construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# para homens: (72.7*h)-58
# para mulheres: (62.1*h)-44.7

print('Olá, para uma avaliação do seu peso ideal, por favor responda as seguintes perguntas: \n')
sexo = str(input('Digite "M" para sexo masculino ou "F" para sexo feminino: '))
sexo = sexo.upper() #convertendo pra maiusculo caso o usuario digite f ou m
print()
altura = float(input('Digite sua altura, ex:(1.77, 1.55, 1.90):  '))

if sexo == 'M':
    peso = (72.7 * altura) - 58
elif sexo == 'F':
    peso = (62.1 * altura) - 44.7
else:
    peso = None
    print('Sexo indefinido, tente novamente!')
if peso != None:
    print(f'Seu peso ideal é: {peso:.3f}kg')
