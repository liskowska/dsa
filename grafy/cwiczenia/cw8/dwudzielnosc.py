"""
Proszę zaimplementować następujące algorytmy:
1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS)
"""
"""
złożoność O(V+E)
"""


from collections import deque
def BFS_duality(s, G): #zakladam, ze graf jest spojny
    n = len(G)
    Q = deque()

    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    d = [float('inf') for _ in range(n)]
    colour = [0 for _ in range(n)]

    d[s] = 0
    visited[s] = True
    Q.append(s)
    colour[s] = 1
    prev_colour = 1

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                Q.append(v)
                colour[v] = colour[u] - 1
    #sprawdzanie dwudzielnosci O(E)
    for v in range(n):
        for u in G[v]:
            if colour[v] == colour[u]: return False
    return True


# graf, ktory ma dwa cykle 0-1-2-0 i 3-4-5-3
G1 = [
    [1, 2],    # 0
    [0, 2],    # 1
    [0, 1, 3], # 2 — cykl: 0–1–2–0
    [2, 4, 5], # 3
    [3, 5],    # 4
    [3, 4]     # 5 — cykl: 3–4–5–3
]

# graf który ma jeden cykl 1-2-3-4-1; cykl czterech wierzchołków
G2 = [
    [1],       # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [2, 4],    # 3
    [3, 1]     # 4 — cykl: 1–2–3–4–1
]

# graf bez cyklu
G3 = [
    [1],       # 0
    [0, 2],    # 1
    [1, 4],       # 2
    [4],       # 3
    [2, 3]        # 4
]

# graf z jednym cyklem czterech wierzchołków
G4 = [
    [1, 3],    # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [0, 2],    # 3 — cykl: 0–1–2–3–0
    [1, 5],    # 4
    [4]        # 5
]

print(BFS_duality(0 ,G1))
print(BFS_duality(0 ,G2))
print(BFS_duality(0 ,G3))
print(BFS_duality(0 ,G4))
