"""
O(n)
Y[i] = liczba punktów, których współrzędna y jest większa lub równa i
X[i] = liczba punktów, których współrzędna x jest większa lub równa i
dominance[i] = X[x-1] + Y[y-1] - (n-1) (z zasady włączeń i wyłączeń)
"""
from egz2atesty import runtests
def dominance(P):
    n = len(P)

    X = [0 for _ in range(n+1)]
    Y = [0 for _ in range(n+1)]
    for x, y in P:
        X[x] += 1
        Y[y] += 1

    for i in range(1, n+1):
        X[i] += X[i-1]
        Y[i] += Y[i-1]

    #zasada włączeń i wyłączeń
    #|X*Y| = |X| + |Y| - |XuY|
    #|XuY| = n-1
    max_dominance = 0
    for x, y in P:
        dominance = X[x-1] + Y[y-1] - (n-1)
        max_dominance = max(max_dominance, dominance)
    return max_dominance

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )