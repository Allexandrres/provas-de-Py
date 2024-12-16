def media(n1, n2, n3):
    media_aritmetica = (n1 + n2 + n3) / 3
    return media_aritmetica

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado = media(numero1, numero2, numero3)
print(f"A média aritmética dos números fornecidos é: {resultado:.2f}")
