"""
Dana jest mapa kraju w postaci grafu G = (V, E). Kierowca chce przejechać
z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne. Każda droga ma taką
samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak najmniejszej liczby
opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla grafu nieskierowanego.

Zadanie jest niedoprecyzowane, wiec zakladam, ze graf jest w postaci macierzowej, gdzie
 G[u][v] = inf --> miedzy u a v nie ma drogi
 G[u][v] = 0  ---> miedzy u a v jest bezplatna droga
 G[u][v] = 1  ---> miedzy u a v jest platna droga
"""

"""
Zadanie znajduje sie w zestawie z BFS i DFS, wiec zakladam, ze nie moge uzyc Dijkstry.
"""

from collections import deque
def BFS_matrix(G, s, t):
    n = len(G)
    Q = deque()

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in range(n):
            if G[u][v] != float('inf') and not visited[v]: #zmiana z != 0 na != float('inf')!!!
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)

    return parent

def cheapest_path(G, s, t):
    parents = BFS_matrix(G, s, t)

    def shortest_path(s, t, parents):
        path = []
        current = t
        while current is not None:
            path.append(current)
            if current == s: break
            current = parents[current]

        path.reverse()
        if path[0] != s: return None
        else: return path

    cheapestpath = shortest_path(s, t, parents)
    return cheapestpath

G = [[float('inf'), 0, 0, 1, float('inf'), float('inf')],
     [float('inf'), float('inf'), 0, float('inf'), float('inf'), 1],
     [1, 1, float('inf'), float('inf'), 1, float('inf')],
     [float('inf'), float('inf'), 0, float('inf'), float('inf'), 1],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), 0],
     [float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]]
print(cheapest_path(G, 0, 5))