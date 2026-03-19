# O meu saldo inicial é $1000,00
# Preciso mostrar o menu de opções que são:
# 1- Ver saldo / 2 - Sacr / 0 - Sair
# Se a pessoa quizer sacar, preciso saber o valor
# Se sacar abaixo de $1000, preciso mostrar o saldo restante
# Se tentar sacar acima de $1000, dixer que é Saldo insuficiente
# O saque precisa verificar duas coisas: o valor a sacar e se tem saldo suficiente
Saldo = 1000
while True:
    print("1 - Ver Saldo")
    print("2 - Sacar")
    print("0 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print(f"Seu saldo é R$ {Saldo}")
    elif opcao == 2:
        valor = float(input("Digite o valor: "))
        if valor <= Saldo: 
            Saldo -= valor
            print("Saque realizado")
        else: 
            print("Saldo insuficiente")
    elif opcao == 0:
        break