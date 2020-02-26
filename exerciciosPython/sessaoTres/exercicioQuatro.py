maior = -999
menor = 999
soma = 0

for contador in range(0, 10):
    receberValor = int(input("Insira um valor: "))
    if receberValor > 0:
        if receberValor > maior:
            maior = receberValor
        if receberValor < menor:
            menor = receberValor
        soma = soma + receberValor
    else:
        receberValor = int(input("Insira um valor: "))
media = soma/10

print("O maior valor é {0}".format(maior))
print("O menor valor é {0}".format(menor))
print("A média é {0}".format(media))
