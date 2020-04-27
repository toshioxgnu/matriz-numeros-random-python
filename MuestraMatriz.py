
def MuestrMatriz(M):
    print("entre MuestrMatriz")
    for i in range(len(M)):
        print ("[")
        for j in range (len(M[i])):
            print (format(M[i][j]))
        print("]")
