def maior_numero(n1, n2, n3):
    # Comparando os três números e retornando o maior
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultado = maior_numero(numero1, numero2, numero3)
print(f"O maior número entre os fornecidos é: {resultado}")
  
