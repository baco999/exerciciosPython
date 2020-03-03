pesoPeixes = float(input("Insira o peso dos peixes: "))

if pesoPeixes > 50:
    excesso = pesoPeixes - 50
    multa = excesso * 4
    print("Peso excedido : {0}".format(excesso))
    print("Valor da multa a pagar : {0}".format(multa))
else:
    print("Peso nao excedido")

print("Peso total : {0}".format(pesoPeixes))
