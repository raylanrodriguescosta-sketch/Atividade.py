

n1 = float(input("Digite o primeiro número positivo: "))
n2 = float(input("Digite o segundo número positivo: "))

print("\nMENU")
print("1 - Média ponderada")
print("2 - Quadrado da soma dos 2 números")
print("3 - Cubo do menor número")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    media = (n1 * 2 + n2 * 3) / 5
    print("Média ponderada:", media)

elif opcao == 2:
    resultado = (n1 + n2) ** 2
    print("Quadrado da soma:", resultado)

elif opcao == 3:
    if n1 < n2:
        menor = n1
    else:
        menor = n2

    cubo = menor ** 3
    print("Cubo do menor número:", cubo)

else:
    print("Opção inválida")