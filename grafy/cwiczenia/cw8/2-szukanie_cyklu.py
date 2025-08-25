"""
Dany jest graf nieskierowany G zawierający n wierzchołków. Zaproponuj
algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie 4 wierzchołków. Zakładamy, że
graf reprezentowany jest przez macierz sasiedztwa A.
"""

"""
Idziemy DFSem wgłąb do długości 4 i w tym momencie sprawdzamy, czy mozemy dostać się do wierzchołka od którego 
zaczęliśmy
"""

def findcycle(G):
    visited = [False for _ in range(len(G))]
    def dfs(G, v, parent):
        visited[v] = True
        for u in G[v]:
            if not visited[u]:
                if dfs(G, u, v): return True
            elif u != parent: return True
        return False

    return dfs(G, 0, -1)

def find4cycle(G):
    visited = [False for _ in range(len(G))]
    def dfs(G, v, parent, depth):
        if depth == 4:
            if visited[v] == True: return True
            else: return False

        for u in G[v]:
            if not visited[u]: dfs(G, u, v, depth + 1)

    for u in range(len(G)):
        if dfs(G, u, -1, 0): return True
    return False

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
    [0, 2],    # 1
    [1, 3],    # 2
    [2, 4],    # 3
    [3, 1]     # 4 — cykl: 1–2–3–4–1
]

# graf bez cyklu
G3 = [
    [1],       # 0
    [0, 2],    # 1
    [1],       # 2
    [4],       # 3
    [3]        # 4
]

# graf z jednym cyklem czterech wierzchołków
G = [
    [1, 3],    # 0
    [0, 2, 4], # 1
    [1, 3],    # 2
    [0, 2],    # 3 — cykl: 0–1–2–3–0
    [1, 5],    # 4
    [4]        # 5
]


print(find4cycle(G1))
print(find4cycle(G2))
print(find4cycle(G3))
print(find4cycle(G))

print(findcycle(G1))
print(findcycle(G2))
print(findcycle(G3))
