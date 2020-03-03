numeroDeHoras = int(input("Insira o numero de horas trabalhadas :"))
salarioHora = 10
salarioHoraExcedente = 20

if numeroDeHoras > 50:
    excessoDePagamento = (numeroDeHoras - 50) * salarioHoraExcedente
    salario = (50 * salarioHora) + excessoDePagamento
    print("Salario R$ {0}".format(salario))
    print("Horas extras R$ {0}".format(excessoDePagamento))
else:
    salario = numeroDeHoras * salarioHora
    horaExtra = 0
    print("Salario R$ {0}".format(salario))
    print("Horas extras R$ {0}".format(horaExtra))