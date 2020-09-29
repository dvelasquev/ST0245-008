matriz = [[1,2,2,3,4],[1,2,3,3,4,5],[3,4,4,4,4,6],[4,5,6,7,8,9]]
def ElementoMatriz(mat,elemento):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == elemento:
                return True
    return False
for i in range(11):
    print(i, ':',ElementoMatriz(matriz,i))
