"""
Algorytm przeszukiwania wgłąb (depth-first search)

Założenia:
Każdy graf ma pole visited, pole parent i czas przetworzenia (?)

Złożoność czasowa:
O(V+E) dla reprezentacji listowej
O(V^2) dla reprezentacji macierzowej

Zastosowania:
1. Wszystko co BFS poza sprawdzaniem najkrótszej ścieżki
2. Sortowanie topologiczne
3. Znajdowanie cyklu Eulera
4. Znajdowanie silnie wspólnej składowej
5. Znajdowanie mostów i punktów artykulacji w grafach nieskierowanych
"""

def DFS_list(G):
    time = 0
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, v):
        nonlocal time
        visited[v] = True
        time += 1
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFS_visit(G, u)
        time += 1

    for v in G:
        if not visited[v]: DFS_visit(G, v)

    return visited, time, parent

def DFS_matrix(G):
    time = 0
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]

    def DFS_visit(G, v):
        nonlocal time
        visited[v] = True
        time += 1
        for u in range(n):
            for v in G[u]:
                if G[v][u] == 1 and not visited[u]: DFS_visit(G, u)
        time += 1

    for v in range(n):
        if not visited[v]: DFS_visit(G, v)

    return visited, time, parent