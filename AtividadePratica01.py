#1- Programa de Saudação
# Crie um programa que imprima a mensagem "Olá, mundo!" na tela. 

print("olá Mundo") 

print("----------------------------------------------")

# 2- Calculadora de Soma
# Desenvolva um programa que soma dois números. Use as variáveis numero1 = 12 e numero2 = 14. O programa deve calcular a soma e exibir o resultado. 

numero1 = 12 
numero2 = 14 
soma = numero1 + numero2

print("A soma de", numero1, "com", numero2, "é", soma) 

print("----------------------------------------------")

# 3- Calculadora de Volume
# Crie um programa que calcula o volume de uma caixa retangular. Use as seguintes dimensões:

# Comprimento: 12 cm
# Largura: 14 cm
# Altura: 20 cm
# O programa deve calcular o volume e exibir o resultado em cm³.

comprimento = 12
largura = 14
altura = 20 
volume = comprimento*largura*altura 

print(f"O volume de uma caixa que tem {comprimento}cm de comprimento {largura}cm de largura e {altura}cm de altura é {volume}cm³!")

print("----------------------------------------------")

# 4- Calculadora de Preço Total
# Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.  

nomeProduto = "Cadeira Infantil"
precoUnitario = 12.40
quantidade = 3 
precoTotal = precoUnitario*quantidade

print("Produto:", nomeProduto, f"\nPreço do produto: R${precoUnitario} \nQuantidade comprada:", quantidade, f"\nTotal da compra: R${precoTotal}")
