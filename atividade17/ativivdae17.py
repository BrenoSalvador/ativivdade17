status = int(input("""
    digite o status em numeros
    1 - IDOSO
    2 - GESTANTE
    3 - CADEIRANTE
    4 - NENHUMA DAS OPÇÕES
"""))

if status == 1:
    print("IDOSO")
elif status == 2:
    print("GESTANTE")
elif status == 3:
    print("CADEIRANTE")
elif status == 4:
    print("NENHUM DAS OPÇÕES")
else:
    print("valor invalido")