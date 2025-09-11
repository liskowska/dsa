"""
O(VE + V^2) ==> O(VE)??
"""
from egz3atesty import runtests
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

    return d

def mykoryza( G,T,d ):
    d = T[d]
    grzyb = [-1 for _ in range(len(G))]
    cur_min_dist = [float("inf") for _ in range(len(G))]
    for v in T:
        cur_dist = BFS_list(v, G)
        for u in range(len(cur_dist)):
            if cur_dist[u] < cur_min_dist[u]:
                cur_min_dist[u] = cur_dist[u]
                grzyb[u] = v
    cnt = 0
    for i in grzyb:
        if i == d: cnt += 1
    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )

# G = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
# T = [8, 2, 6]
# d = 1
# print(mykoryza2(G, T, d))