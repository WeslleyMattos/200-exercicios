#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: ?São múltiplos? ou ?Não são múltiplos?. 

a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))

if a % b == 0 or b % a == 0: #tem q dar zero
    print("São múltiplos")
else:
    print("Não são múltiplos")

    #Exercicio 2 e 20 sao praticamente mema coisa