"""
Mówimy, że wierzchołek t w grafie skierowanym jest uniwersalnym
ujściem, jeśli
(a) z każdego innego wierzchołka v istnieje krawędź z v do t, oraz
(b) nie istnieje żadna krawędź wychodząca z t.
1. Podać algorytm znajdujący uniwersalne ujście (jeśli istnieje) przy reprezentacji macierzowej (O(n^2)).
2. Pokazać, że ten problem można rozwiazac w czasie O(n)
"""

"""
Uwaga 1. W grafie może być tylko jedno uniwersalne ujście
Uwaga 2. W postaci macierzowej uniwersalne ujście będzie wyglądało tak, że w pionie G[x][u] będą
same 1 i jedno 0 na pozycji G[u][u], gdzie u wierzcholek bedacy uniwersalnym ujsciem.
"""

#O(n^2)
def universal_sink(G):
    n = len(G)
    sink = -1
    for i in range(n):
        for j in range(n):
            if i == j:
                if j != n-1: continue
            if G[i][j] == 1: break #przechodze do nastepnego wiersza
            if j == n-1 and G[i][j] == 0: #jesli jestem w ostatniej kolumnie i dalej wszystko sie zgadza
                sink = i
    for k in range(n):
        if G[k][sink] == 0 and sink != k: return None
    return sink

#O(n)
def universal_sink2(G):
    n = len(G)
    i = 0
    j = 0
    while i < n and j < n:
        if G[i][j] == 1:
            i += 1  # i nie może być ujściem
        else:
            j += 1  # j nie może być ujściem
    if i >= n: return None

    for k in range(n):
        if i == k: continue
        if G[i][k] != 0: return None
    return i


G = [[0, 1, 1, 0, 1],
     [1, 0, 1, 0, 1],
     [0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0],
     [0, 1, 1, 0, 0]]

G2 = [
    [0, 1, 1, 1],  # 0 → 1, 2, 3
    [0, 0, 1, 1],  # 1 → 2, 3
    [0, 0, 0, 1],  # 2 → 3
    [0, 0, 0, 0]   # 3 → nikt (ujście uniwersalne)
]


print(universal_sink(G))
print(universal_sink(G2))

print(universal_sink2(G))
print(universal_sink2(G2))