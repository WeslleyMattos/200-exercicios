# Calcule a média aritmética das 3 notas de um aluno e mostre, além do valor da média, uma mensagem de "Aprovado", caso a média seja igual ou superior a 6, ou a mensagem "reprovado", caso contrário.

print('Digite 3 notas suas da matéria para saber se foi aprovado ou reprovado: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira notas: '))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print(f'Parabéns você foi aprovado! Passando com uma média de {media:.2f}.')
else:
    print(f'Reprovado! Estude mais!! Sua média foi apenas {media:.2f}.')
