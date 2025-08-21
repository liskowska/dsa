"""
Złożoność akceptowalna O(VElog*E) (4,95s)
9/12 testów w 2s
Algorytm najpierw zamienia listę sąsiedztwa na listę krawędzi, a następnie sortuje ją od najmniejszej
do największej krawędzi. Następnie próbuje tworzyć piękne drzewo z KOLEJNYCH krawędzi, czyli w momencie
znalezienia cyklu (find(v) = find(u)) dalsze tworzenie drzewa nie ma sensu, bo nie będzie już spełniać
warunków zadania. Przechodzę więc przez krawędzie i zaczynając od coraz większej krawędzi próbuję stworzyć
drzewo o coraz większej wartości. Jeśli się uda - zwracam jego wagę, jeśli nie - próbuję dalej. DLa lekkiej
optymalizacji dodałam licznik pozostałych krawędzi z których mogę zrobić drzewo. Jeżeli zostało mniej
niż |V|-1 krawędzi stworzenie żadnego drzewa już nie jest możliwe, więc zwracam None.
"""

from kol2testy import runtests

def to_edges(G):
    edges = []
    n = len(G)
    for v in range(n):
        for u, w in G[v]:
            if v > u: continue
            edges.append((v, u, w))
    return edges, n

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, rank, x, y):
    x = Find(parent, x)
    y = Find(parent, y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def create_beutree(G, n, i):
    parent = [_ for _ in range(n)]
    rank = [1 for _ in range(n)]
    taken = 0
    cnt = 0

    for e in range(i, len(G)):
        if taken == n - 1:
            return cnt
        x = Find(parent, G[e][0])
        y = Find(parent, G[e][1])

        if x == y: return -1
        if x != y:
            Union(parent, rank, x, y)
            taken += 1
            cnt += G[e][2]
    return -1

def beautree(G):
    E, n = to_edges(G)
    E.sort(key=lambda x: x[2])
    ans = -1
    m = len(E)
    for i in range(len(E)):
        m -= 1
        if m < n-1: return None
        ans = create_beutree(E, n, i)
        if ans == -1: continue
        else: return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
