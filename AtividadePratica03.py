"""1- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias: 
*Criança (0-12 anos), 
*Adolescente (13-17 anos), 
*Adulto (18-59 anos) ou 
*Idoso (60 anos ou mais)."""
print("Classificador de Idade")
idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida.")
elif idade <= 12:
    print("Você é uma Criança.")
elif idade <= 17:
    print("Você é um(a) Adolescente.")
elif idade <= 59:
    print("Você é um(a) Adulto(a).")
else:
    print("Você é um(a) Idoso(a).") 
print("-------------------------------------")
"""2- Calculadora de IMC 
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.
< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = 'Obeso'"""
print("Calculadora de IMC")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}") 
print("-------------------------------------")
"""3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.""" 
print("Conversor de Temperatura")

def celsius_para_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").strip().upper()
destino = input("Unidade de destino (C, F ou K): ").strip().upper()

resultado = None

if origem == "C":
    if destino == "F":
        resultado = celsius_para_fahrenheit(temp)
    elif destino == "K":
        resultado = celsius_para_kelvin(temp)
    elif destino == "C":
        resultado = temp
elif origem == "F":
    if destino == "C":
        resultado = fahrenheit_para_celsius(temp)
    elif destino == "K":
        resultado = fahrenheit_para_kelvin(temp)
    elif destino == "F":
        resultado = temp
elif origem == "K":
    if destino == "C":
        resultado = kelvin_para_celsius(temp)
    elif destino == "F":
        resultado = kelvin_para_fahrenheit(temp)
    elif destino == "K":
        resultado = temp
else:
    print("Unidade de origem inválida.")

if resultado is not None:
    print(f"{temp}°{origem} é igual a {resultado:.2f}°{destino}")
print("-------------------------------------") 

"""4- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não. Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.""" 
print("Verificador de Ano Bissexto")
def verificar_ano_bissexto(ano):
    if (ano % 400 == 0):
        return True
    elif (ano % 100 == 0):
        return False
    elif (ano % 4 == 0):
        return True
    else:
        return False

ano = int(input("Digite um ano: "))
if verificar_ano_bissexto(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")
