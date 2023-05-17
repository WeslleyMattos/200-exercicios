#Calcular o salário bruto, o desconto do INSS (8,5% do salário bruto) e o salário família.

num_dependentes = int(input("Digite o número de dependentes: "))
salario_base = float(input("Digite o salário base: "))

desconto_inss = salario_base * 0.085

salario_familia = 0
if salario_base <= 907.77:  # Seu salario tem que ser no maximo isso para receber o auxilio familia.
    salario_familia = num_dependentes * 48.62

salario_bruto = salario_base - desconto_inss + salario_familia

print("Salário Bruto: R$", salario_bruto)
print("Desconto do INSS: R$", desconto_inss)
print("Salário Família: R$", salario_familia)
