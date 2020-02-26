identificador = int(input("Insira a identificação: "))
quantidade = 0
necessitaEsfera = 0
necessitaLimpeza = 0
necessitaTrocaCabo = 0
quebrado = 0

while identificador != 0:
    print("Identifique o defeito")
    print("1 - Necessita da esfera")
    print("2 - Necessita da limpeza")
    print("3 - Necessita da troca do cabo")
    print("4 - Quebrado")
    defeito = int(input("Insira o defeito: "))
    if defeito == 1:
        necessitaEsfera = necessitaEsfera + 1
    elif defeito == 2:
        necessitaLimpeza = necessitaLimpeza + 1
    elif defeito == 3:
        necessitaTrocaCabo = necessitaTrocaCabo + 1
    elif defeito == 4:
        quebrado = quebrado + 1
    quantidade = quantidade + 1

    identificador = int(input("Insira a identificação: "))

percentualEsfera = (necessitaEsfera / quantidade) * 100
percentualLimpeza = (necessitaLimpeza / quantidade) * 100
percentualTrocaCabo = (necessitaTrocaCabo / quantidade) * 100
percentualQuebrado = (quebrado / quantidade) * 100

print("Quantidade de mouses {0}".format(quantidade))
print("Situação                         Quantidade             Porcentual")
print("1 = Necessidade de esfera            {0}                    {1}%".format(necessitaEsfera, percentualEsfera))
print("2 = Necessidade de limpeza           {0}                    {1}%".format(necessitaLimpeza, percentualLimpeza))
print("1 = Necessidade de troca de cabo     {0}                    {1}%".format(necessitaTrocaCabo, percentualTrocaCabo))
print("1 = Quebrado                         {0}                    {1}%".format(quebrado, percentualQuebrado))