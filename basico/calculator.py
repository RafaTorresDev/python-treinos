#calculaora com while

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite um segundo número: "))
        operador = input("Qual operador voçê deseja(+-*/): ")

        if operador == '+':
            print(f"{num1 + num2}")
        elif operador == '-':
            print(f"{num1 - num2}")
        elif operador == '*':
            print(f"{num1 * num2}")
        elif operador == '/':
            print(f"{num1 / num2}")
        else:
            print("OPERADOR INVÁLIDO")

    except:
        print("VALOR INVÁLIDO!")

    sair = input("Dejesa finalizar o programa? [s][n]").lower().startswith("s")

    if sair == True:
        break