"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada""" 

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor_conta = 100.0
porcentagem_gorjeta = 10.0
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
print(f"Valor da conta: R${valor_conta:.2f}")
print(f"Porcentagem de gorjeta: {porcentagem_gorjeta}%")
print(f"Valor da gorjeta: R${gorjeta:.2f}")
print(f"Total a pagar: R${valor_conta + gorjeta:.2f}")
print("------------------------------------")
"""2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

import re

def verificar_palindromo(texto):
    texto = re.sub(r'\W+', '', texto).lower()
    return texto == texto[::-1]

def resposta_palindromo(texto):
    if verificar_palindromo(texto):
        return "Sim"
    else:
        return "Não"

texto = input("Digite uma palavra ou frase: ")
print(resposta_palindromo(texto))
print("------------------------------------")
"""3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado."""

def calcular_desconto(preco, desconto):
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return round(preco_final, 2)

def main():
    preco = float(input("Digite o preço do produto: R$ "))
    desconto = float(input("Digite o percentual de desconto (%): "))

    preco_final = calcular_desconto(preco, desconto)
    valor_desconto = round(preco * (desconto / 100), 2)

    print(f"Preço original: R$ {preco:.2f}")
    print(f"Desconto: {desconto}% = R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()
print("------------------------------------")
"""4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.""" 
from datetime import datetime, date

def calcular_idade_em_dias(data_nascimento):
    hoje = date.today()
    idade = hoje - data_nascimento
    return idade.days

def main():
    data_nascimento_str = input("Digite a data de nascimento (no formato YYYY-MM-DD): ")
    ano, mes, dia = map(int, data_nascimento_str.split('-'))
    data_nascimento = date(ano, mes, dia)

    idade_em_dias = calcular_idade_em_dias(data_nascimento)
    print(f"Você está vivo há {idade_em_dias} dias.")

if __name__ == "__main__":
    main()