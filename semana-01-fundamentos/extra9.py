# Menu impresso

while True:
    print("1 - Dizer olá")
    print("2 - Dizer tchau")
    print("0 - Sair")
    opcao  = int(input("Escolha: "))

    if opcao == 1:
        print("Olá!")
    elif opcao == 2:
        print("Tchau!")
    elif opcao == 0:
        break

# Menu não impresso

'''while True:
    opcao = int(input("Escolha entre 0, 1 e 2: "))
    
    if opcao == 1:
        print("Olá!")
    elif opcao == 2:
        print("Tchau!")
    elif opcao == 0:
        break'''