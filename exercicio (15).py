# Faça um algoritmo que leia 2 números reais quaisquer e, a seguir, solicite a operação matemática desejada. 
# Ao final, calcule e mostre o resultado!


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

calculo = input("Qual operação matemática deseja realizar? \nDigite (+) para somar \nDigite (-) para subtrair \
                 \nDigite (*) para multiplicar \nDigite (/) para dividir!\n >>>>>> ")

if calculo == "+":
    resultado = num1 + num2
elif calculo == "-":
    resultado = num1 - num2
elif calculo == "*":
    resultado = num1 * num2
elif calculo == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = None

if resultado != None:
    print("O resultado da operação é:", resultado)

#Link de estudo: https://www.youtube.com/watch?v=K10u3XIf1-Q&t=1527s&ab_channel=CursoemV%C3%ADdeo