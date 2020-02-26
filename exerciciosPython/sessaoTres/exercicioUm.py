maior = 0

numero = int(input("Insira um numero: "))

while numero != 0:
    if numero > maior:
        maior = numero
    numero = int(input("Insira um numero: "))
print("O maior numero é {0}".format(maior))