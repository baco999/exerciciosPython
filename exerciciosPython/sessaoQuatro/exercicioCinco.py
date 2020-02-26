vetor = []
##posicao = 0
maiorQueCinquenta = False

for contador in range(0, 10):
    valor = int(input("Insira {0}/10 valores no vetor".format(contador + 1)))
    vetor.append(valor)

for contador in vetor:
    if contador > 50:
        print("O valor {0} esta na posição do vetor {1}".format(contador, vetor.index(contador)))
        maiorQueCinquenta = True
   ## posicao = posicao + 1
if maiorQueCinquenta == False:
    print("Não existe o maior numero maior que 50")
