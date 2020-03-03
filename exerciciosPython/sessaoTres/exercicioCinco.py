nomeDoUsuario = input("Insira o nome de usuario: ")
senhaDoUsuario = input("Insira sua nova senha: ")

while nomeDoUsuario.casefold() == senhaDoUsuario.casefold():
    print("A senha nao pode ser igual ao nome do usuario")
    nomeDoUsuario = input("Insira o nome de usuario: ")
    senhaDoUsuario = input("Insira sua nova senha: ")

print("Cadastrado com sucesso")

