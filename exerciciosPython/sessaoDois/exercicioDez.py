idadeNadador = int(input("Insira a idade do nadador: "))

if (idadeNadador >= 5) and (idadeNadador <= 7):
    print("Categoria: Infantil A")
elif (idadeNadador > 7) and (idadeNadador <= 11):
    print("Categoria: Infantil B")
elif (idadeNadador > 11) and (idadeNadador <= 13):
    print("Categoria: Juvenil A")
elif (idadeNadador > 13) and (idadeNadador <= 17):
    print("Categoria: Juvenil B")
elif idadeNadador >= 18:
    print("Categoria: Adulto")