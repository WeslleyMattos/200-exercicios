#Escrever um algoritmo que lê 2 valores, a, b, verifica se são múltiplos, e escreve "são múltiplos", ou "não são múltiplos". 
#Dica: considere a existência de um operador MOD cujo resultado é o resto da divisão de um número por outro.

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if a % b == 0 or b % a == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")


#Link de estudo: https://www.youtube.com/watch?v=-RQTFSNWRSc&ab_channel=eXcript