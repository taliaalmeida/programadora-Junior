num1 = float(input("Digite um numero: "))
num2 = float(input("Digite mais um numero: "))
operacao = input("Digite a operação desejada {+, -, *, /}")

if operacao == "+":
    resultado = num1 + num2
    print(resultado)
elif operacao == "-":
    resultado = num1 - num2
    print(resultado)
elif operacao == "*":
    resultado = num1 * num2
    print(resultado)
elif operacao == "/":
    if num2 ==0:
        print(" Erro: divisão por zero!")
    else:
        resultado = num1 / num2
        print(resultado)
else:
    print("Digite a operação correta!")
