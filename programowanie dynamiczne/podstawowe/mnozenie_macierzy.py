# Zadanie 4. (mnożenie macierzy)
# Dany jest cięg macierzy A1, A2, . . . , An. Ktoś chce policzyć iloczyn
# A1A2⋯An. Macierze nie sa koniecznie kwadratowe (ale oczywiście znamy ich rozmiary). Zależnie w jakiej
# kolejnosci wykonujemy mnożenia, koszt obliczeniowy moze byc różny—należy podać algorytm znajdujący
# koszt mnożenia przy optymalnym doborze kolejności.

def min_multiplication(P):
    n = len(P)
    C = [[0 for _ in range(n)] for _ in range(n)]
    K = [[0 for _ in range(n)] for _ in range(n)]
    # chcemy isc po ukosnych
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i + d
            mini = float('inf')
            for k in range(i, j):
                q = C[i][k] + C[k+1][j] + P[i-1]*P[k]*P[j]
                if q < mini:
                    mini = q
                    K[i][j] = k
            C[i][j] = mini
    print(C)
    return C[1][n-1]

P = [5, 4, 6, 2, 7]
Q = [3, 2, 4, 2, 5]
R = [2, 3, 2]
print(min_multiplication(P))
print(min_multiplication(Q))
print(min_multiplication(R))
