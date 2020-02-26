vetor = []

for contador in range(0, 10):
    valorUm = int(input("Insira o valor do vetor de 1 a 10: "))
    vetor.append(valorUm)

vetor.reverse()  ##inverte a ordem
for contador in vetor:
    print(contador)
