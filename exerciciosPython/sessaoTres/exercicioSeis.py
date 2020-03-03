numero = int(input("Insira um numero entre 1 e 10: "))

while numero > 10 or numero < 1:
    print("O numero nao pode ser maior ou menos que 10")
    numero = int(input("Insira um numero: "))

print("Tabuado do {0}".format(numero))
for contador in range(1, 11):
    result = numero * contador
    print("{0} X {1} = {2}".format(numero, contador, result))
