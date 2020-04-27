from MuestraMatriz import MuestrMatriz
from CreaMatriz import creaMatriz
print("Inicie")

if __name__ == "__main__":
    print("Ola")
    m=int(input("Ingrese columnas de la matriz: "))
    n=int(input("Ingrese filas de la matriz: "))
    M= creaMatriz(m,n)
    MuestrMatriz(M)
