"""
2. Policzyć liczbę spójnych składowych w grafie (DFS)
"""

def DFS_consistentcomponents(G):
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

    cnt = 0 #
    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)
            cnt += 1 #

    return cnt

# graf spojny z jednym cyklem czterech wierzchołków
G4 = [
    [1, 3],    # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [0, 2],    # 3 — cykl: 0–1–2–3–0
    [1, 5],    # 4
    [4]        # 5
]

# niespojny graf, z dwoma spojnymi skladowymi
G1 = [
    [1],  # 0 ┐
    [0, 2],  # 1 ┼─ spójna składowa A: 0–1–2
    [1],  # 2 ┘

    [4, 5],  # 3 ┐
    [3, 5],  # 4 ┼─ spójna składowa B: 3–4–5 (trójkąt)
    [3, 4]  # 5 ┘
]

# niespojny graf z czterema spojnymi skladowymi
G2 = [
    [1],       # 0 ┐
    [0],       # 1 ┘   — komponent A: 0–1

    [3],       # 2 ┐
    [2],       # 3 ┘   — komponent B: 2–3

    [],        # 4     — komponent C: samotny wierzchołek

    [6, 7],    # 5 ┐
    [5, 7],    # 6 ┼─   — komponent D: 5–6–7 (trójkąt)
    [5, 6]     # 7 ┘
]

print(DFS_consistentcomponents(G1))
print(DFS_consistentcomponents(G2))
print(DFS_consistentcomponents(G4))