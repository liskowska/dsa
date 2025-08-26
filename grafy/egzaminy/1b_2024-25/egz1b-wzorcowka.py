from egz1Btesty import runtests
from math import inf as INF


def to_adj(V, E):
    graph = [[] for _ in range(V)]
    for v, u in E:
        graph[v].append(u)
    return graph


from collections import deque
def BFS_list(G, s):
    n = len(G)
    Q = deque()

    visited = [False for _ in range(n)]
    visited[s] = True
    Q.append(s)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                Q.append(v)
    return visited

def BFSxV(G, V):
    canReach = [[False for _ in range(V)] for _ in range(V)]

    for v in range(V):
        canReach[v]= BFS_list(G, v)
    return canReach

def critical(V, E):
    graph= to_adj(V, E)        #O(E)
    critical_cnt = 0
    canReach = BFSxV(graph, V)              #O(V(E+V))

    # sprawdzam, czy z v do u istenieje ścieżka inna niż ta bezpośrednia
    for v, u in E:                          #0(VE)
        alternative_path = False
        for x in range(V):
            if v != x and x != u and canReach[v][x] and canReach[x][u]:
                alternative_path = True
                break

        if not alternative_path: critical_cnt += 1
    return critical_cnt


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests=True)