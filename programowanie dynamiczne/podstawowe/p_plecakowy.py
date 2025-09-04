# Proszę podać i zaimplementować algorytm znajdujący wartość optymalnego zbioru przedmiotów w dyskretnym
# problemie plecakowym. Algorytm powinien działać w czasie wielomianowym względem liczby przedmiotów
# oraz sumy ich profitów.

# ang. 0/1 knapsack problem

def knapsack(A,  n):
    m = len(A)
    V = [[0 for _ in range(n+1)] for _ in range(m + 1)]

    for i in range (1, m+1):
        wage, value = A[i - 1]
        for j in range(n+1):
            if j - wage >= 0:
                V[i][j] = max(V[i-1][j], V[i-1][j-wage] + value)
            else:
                V[i][j] = V[i-1][j]
    return V[m][n]

A = [(12, 4), (2, 2), (1, 2), (1, 1), (4, 10)]
B = [(1, 2), (2, 3), (5, 4), (6, 5)]
print(knapsack(A, 4))
print(knapsack(B, 8))

