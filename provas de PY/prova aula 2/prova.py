nome = input("Digite o nome do contato: ")
telefone = input("Digite o número de telefone: ")
email = input("Digite o endereço de email: ")

contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email
}

print("\nInformações do contato:")
print("Nome:", contato["nome"])
print("Telefone:", contato["telefone"])
print("Email:", contato["email"])