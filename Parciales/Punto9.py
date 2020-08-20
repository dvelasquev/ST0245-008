def SeriePascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    elif row < column:
        return 0
    else:
        return SeriePascal(row-1, column-1) + SeriePascal(row-1, column)

def aux(n):
    for x in range(n):
        for z in range(x+1):
            print(SeriePascal(x, z), "", end="")
        print()

n=int(input("¿Cuantas filas tiene el tríangulo de pascal que quiere crear? "))
aux(n)