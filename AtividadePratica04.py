"""1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)."""
def calculadora():
    print("Calculadora Simples")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")

    operacao = input("Escolha a operação (1/2/3/4): ")

    if operacao in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if operacao == '1':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")
        elif operacao == '2':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")
        elif operacao == '3':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")
        elif operacao == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            else:
                print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

calculadora()
print("--------------------------------")
print
"""2 - Criar um código que registre as notas de alunos e calcular a média da turma."""
notas = {}

while True:
    print("1. Adicionar nota")
    print("2. Calcular média de um aluno")
    print("3. Calcular média da turma")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota: "))

        if nome in notas:
            notas[nome].append(nota)
        else:
            notas[nome] = [nota]

        print(f"Nota adicionada com sucesso para o aluno {nome}!")

    elif opcao == '2':
        nome = input("Digite o nome do aluno: ")
        if nome in notas:
            media = sum(notas[nome]) / len(notas[nome])
            print(f"A média do aluno {nome} é {media:.2f}")
        else:
            print("Aluno não encontrado!")

    elif opcao == '3':
        soma_medias = 0
        for aluno in notas:
            soma_medias += sum(notas[aluno]) / len(notas[aluno])
        media_turma = soma_medias / len(notas)
        print(f"A média da turma é {media_turma:.2f}")

    elif opcao == '4':
        break

    else:
        print("Opção inválida!")
print("--------------------------------")
"""3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número."""
def verificar_senha(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

senha = input("Digite uma senha: ")

if verificar_senha(senha):
    print("Senha válida!")
else:
    print("Senha inválida. A senha deve ter pelo menos 8 caracteres e conter pelo menos um número.")
print("--------------------------------")
"""4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos."""
pares = 0
impares = 0

while True:
    num = input("Digite um número (ou 'sair' para finalizar): ")
    if num.lower() == 'sair':
        break
    try:
        num = int(num)
        if num % 2 == 0:
            pares += 1
            print(f"{num} é par!")
        else:
            impares += 1
            print(f"{num} é ímpar!")
    except ValueError:
        print("Valor inválido! Por favor, digite um número.")

print(f"\nTotal de números pares: {pares}")
print(f"Total de números ímpares: {impares}")