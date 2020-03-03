num1 = int(input("Insira um numero: "))

if num1 % 2 == 0:
    if num1 > 0:
        print("O numero inserido é par e positivo {0}".format(num1))
    else:
        print("O numero inserido é par e negativo {0}".format(num1))
if num1 % 2 != 0:
    if num1 > 0:
        print("O numero inserido é impar e positivo {0}".format(num1))
    else:
        print("O numero inserido é impar e negativo {0}".format(num1))

