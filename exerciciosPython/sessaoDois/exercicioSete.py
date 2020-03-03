import math;
n1 = int(input("Insira o primeiro numero :"))
n2 = int(input("Insira o segundo numero :"))
n3 = int(input("Insira o terceiro numero :"))
n4 = int(input("Insira o quarto numero :"))

n1 = math.pow(n1,2)
n2 = math.pow(n2,2)
n3 = math.pow(n3,2)
n4 = math.pow(n4,2)

if n3 >= 1000:
    print("O valor do terceiro numero ao quadrado é {0}".format(n3))
else:
    print("{0}, {1}, {2}".format(n1, n2, n4))
