#Escreva um algoritmo que “valide” uma nota de prova de um aluno informada via teclado (entre 0 e 10)
#como “nota válida” ou “nota inválida

nota = float(input("Digite a nota da prova (entre 0 e 10): "))

if nota >= 0 and nota <= 10:
    print("Nota válida!")
else:
    print("Nota inválida!")
