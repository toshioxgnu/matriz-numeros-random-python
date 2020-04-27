import random

def creaMatriz(m,n):
    print("Entre creaMatriz")
    matriz=[[],[]]
    for i in range (0,m):
        for j in range(0,n):
            matriz[i][j]=random.randrange(100)
            
    return matriz
