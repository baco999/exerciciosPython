nivelDePoluicao = float(input("Insira o nivel de poluição: "))

## & == and
if (nivelDePoluicao >= 0.3) and (nivelDePoluicao < 0.4):
    print("Grupo 1 suspender as atividades")
elif (nivelDePoluicao >= 0.4) and (nivelDePoluicao < 0.5):
    print("Grupo 1 e 2 suspender as atividades")
elif nivelDePoluicao >= 0.5:
    print("Todos os grupos suspender as atividades")
else:
    print("Niveis aceitaveis")