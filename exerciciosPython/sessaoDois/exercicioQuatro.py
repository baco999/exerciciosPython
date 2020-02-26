altura = float(input("Insira sua altura: "))
sexo = input("Insira seu sexo (M ou F): ")
masc = "M"
femi= "F"

##Lower serve para converter String de entrada em minusculo
if sexo.casefold() == masc.casefold():
    pesoIdeal = (altura * 72.7) - 58
elif sexo.casefold() == femi.casefold():
    pesoIdeal = (altura * 62.1) - 44.7
else:
    print("Valores invalidos")

print("Seu peso ideal é {0:.2f}".format(pesoIdeal))
