nota1 = float(input("Digite suaa primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = nota1 + nota2 / 2

print(f"Sua média é {media}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")    