# 7	O cardápio de uma casa de lanches é dado pela tabela abaixo:
# CÓDIGO	ESPECIFICAÇÃO	PREÇO UNITÁRIO
# 100	cachorro quente	1,70
# 101	bauru simples	2,30
# 102	bauru com ovo	2,60
# 103	hamburguer	2,40
# 104	X-burguer	2,50
# 105	refrigerante	1,00
# Escrever um algoritmo que lê código do item adquirido por um consumidor e a quantidade, calculando e mostrando o valor a pagar. 

print('Bem vindo! Aqui a tabela com os nossos produtos:')
print('\nCÓDIGO	ESPECIFICAÇÃO	PREÇO UNITÁRIO \
\n100	cachorro quente	1,70 \
\n101	bauru simples	2,30 \
\n102	bauru com ovo	2,60 \
\n103	hamburguer	2,40 \
\n104	X-burguer	2,50 \
\n105	refrigerante	1,00 ')

cardapio = [
    [100, "cachorro quente", 1.70],
    [101, "bauru simples", 2.30],
    [102, "bauru com ovo", 2.60],
    [103, "hamburguer", 2.40],
    [104, "X-burguer", 2.50],
    [105, "refrigerante", 1.00] #aqui criei um array pra salvar a tabelinha com os dados
]

codigo = int(input("\nDigite o código do item desejado: "))
quantidade = int(input("Digite a quantidade desejada: "))

preco_item = 0 #define preço item pra zero
for item in cardapio: 
    if item[0] == codigo: #se o item na posição 0 for igual ao codigo ele retorna
        preco_item = item[2] # o preço do item que ta na posição 2 do array ↑
        break #para o laço

if preco_item == 0: #como defini ali em cima que o preço do item pra zero, se oq o usuario digitar for igual a zero ou diferente ele da erro, senão ele pega o valor dado pelo laço e faz o calculo de quantidade x valor.
    print("Código inválido.")
else:
    valor_total = preco_item * quantidade

    print(f"O valor total a pagar é de R${valor_total:.2f}.")


#Link de estudo: https://www.youtube.com/watch?v=m4XgtArpc-8&ab_channel=HashtagPrograma%C3%A7%C3%A3o