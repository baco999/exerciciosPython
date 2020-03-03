vetorUm = []
vetorDois = []
soma = []

for contador in range(1, 11):
    valorUm = int(input("Insira o valor para o primeiro vetor"))
    vetorUm.append(valorUm)
    valorDois = int(input("Insira o valor para o segundo vetor"))
    vetorDois.append(valorDois)
    soma.append(valorUm + valorDois)

for contadorDois in soma:
    print(contadorDois)
