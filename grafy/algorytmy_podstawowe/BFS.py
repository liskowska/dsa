"""
Przeszukiwanie grafu wszerz (breadth first search)

Założenia:
Każdy graf ma pole visited, pole parent i pole d(eph) - odległość

Złożoność czasowa:
O(V+E) dla reprezentacji listowej
O(V^2) dla reprezentacji macierzowej

Zastosowania:
1. Znajdowanie najkrótszych ścieżek w grafie
2. Sprawdzanie spójności grafu
3. Sprawdzanie czy graf ma cykl
4. Sprawdzanie czy graf jest dwudzielny
"""

from collections import deque

def BFS_list(s, G):
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
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)

    return visited, parent, d


def BFS_matrix(s, G):
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
            if G[u][v] != 0 and not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)

    return visited, parent, d

# najkrotsza sciezka z s do v
def shortest_path(G, s, v, parents):
    if v == s:
        print(s, end=' ')
    elif parents[v] is None:
        print("sciezka z s do v nie istenieje")
    else:
        shortest_path(G, s, parents[v], parents)
        print(v, end=' ')

