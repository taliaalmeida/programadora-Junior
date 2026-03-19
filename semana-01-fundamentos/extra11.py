tentativas = 3
palavra_secreta = ("Vencedora")

while tentativas > 0:
    palavra = input("Digite a palavra secreta: ")
    if palavra == palavra_secreta:
        print("Parabéns")
        break
    else:
        print("Errou! ")
    tentativas -= 1
else:
    print("Game Over! A palavra era: Vencedora")


