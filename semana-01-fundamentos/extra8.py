codigo_correto = "7"
codigo = int(input("Digite o código correto: "))
while codigo != codigo_correto:
    print("Código incorreto! Tente novamente.")
    codigo = input("Digite o código correto: ")

print("Código correto!")


