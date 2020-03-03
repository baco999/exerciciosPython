vetor = []
##soma = 0

for contador in range(0, 20):
    valor = int(input("Insira {0}/20 valores no vetor : ".format(contador + 1)))
    vetor.append(valor)
## soma = soma + valor
##sum() = soma os valores do vetor
print("O resultado da soma dos vetores é {0}".format(sum(vetor)))
