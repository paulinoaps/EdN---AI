"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""

valorReais = 100.00
taxaDolar = 5.20
taxaEuro = 6.15 

print(f"R${valorReais} em dólar(es) é U${valorReais/taxaDolar:.2f}̣̣\nR${valorReais} em euro(s) é £${valorReais/taxaEuro:.2f}̣")
print("----------------------------------------------------")

"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""

nomeProduto = "Camiseta"
precoOriginal = 50.00
porcentagemDesconto = 20

print(f"Valor com desconto é R${precoOriginal*(1-porcentagemDesconto/100):.2f}")
print("----------------------------------------------------")

"""3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais."""

nota1 =  7.5
nota2 =  8.0
nota3 =  6.5

print(f"Nota 1: {nota1}\nNota 2: {nota2}\nNota 3: {nota3}\nMédia: {(nota3+nota2+nota1)/3:.2f}")
print("----------------------------------------------------")

"""4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.""" 

distanciaPercorrida = 300
combustivelGasto = 25 

print(f"Distância percorrida: {distanciaPercorrida}km\nCombustível gasto: {combustivelGasto} litros\nMédia de consumo: {distanciaPercorrida/combustivelGasto:.2f} km/l")