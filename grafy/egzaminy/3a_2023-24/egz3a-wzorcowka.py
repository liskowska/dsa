from egz3atesty import runtests
from collections import deque

def bfs_mod(G, T):
    n = len(G)
    m = len(T)
    time = [float("inf") for _ in range(n)]
    grzyb = [None for _ in range(n)] # grzyb[i] = j jesli wierzcholek i został zawładnięty grzybem z wierzchołka j
    index = {}
    Q = deque()

    for i in range(m):
        u = T[i]
        time[u] = 0
        grzyb[u] = u
        index[u] = i
        Q.append(u)

    while Q:
        u = Q.popleft()
        t = time[u] + 1
        for v in G[u]:
            if time[v] > t:
                time[v] = t
                grzyb[v] = grzyb[u]
                Q.append(v)
            elif time[v] == t and index[grzyb[v]] > index[grzyb[u]]:
                grzyb[v] = grzyb[u]
                Q.append(v)
    return grzyb

def mykoryza( G,T,d ):
    grzyb = bfs_mod(G, T)
    cnt = 0
    d = T[d]

    for i in grzyb:
        if i == d: cnt += 1

    return cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )

# G = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]
# T = [8, 2, 6]
# d = 1
# print(mykoryza2(G, T, d))