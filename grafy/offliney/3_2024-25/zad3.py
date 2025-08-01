from copy import deepcopy

from zad3testy import runtests

"""
Algorytm w złożoności akceptowalnej O(VE+E^2) polega na usuwaniu każdej krawędzi po kolei i sprawdzanie BFSem, czy
wydłuża to ścieżkę od s do t
"""

from collections import deque
def longer( G, s, t ):

    def BFS_list(G, s, t):
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

        return d[t]

    d = BFS_list(G, s, t)
    for v in range(len(G)):
        for u in G[v]:
            new_graph = deepcopy(G)
            new_graph[v].remove(u)
            new_graph[u].remove(v)
            new_d = BFS_list(new_graph, s, t)
            if new_d != d: return v, u

    return None

def longer2(G, s, t):

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
