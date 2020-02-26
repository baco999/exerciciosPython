vetor = []

codigoNumerico = int(input("Insira o codigo numerico: "))

if codigoNumerico != 0:
    for contador in range(0, 5):
        valor = float(input("Insira o {0}/5 valores no vetor: ".format(contador + 1)))
        vetor.append(valor)

    if codigoNumerico == 1:
        for contador in vetor:
            print("Os valores inseridos no vetor são {0}".format(contador))

    if codigoNumerico == 2:
        vetor.reverse()
        for contador in vetor:
            print("Os valores inseridos nos vetor invertidos sao {0}".format(contador))
