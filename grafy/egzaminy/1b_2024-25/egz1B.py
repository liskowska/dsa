from copy import deepcopy

from egz1Btesty import runtests
from math import inf as INF

def to_adj(V, E):
    graph = [[] for _ in range(V)]
    for v, u in E:
        graph[v].append(u)
    return graph

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

    for v in range(n):
        if not visited[v]: DFS_visit(G, v)

    return visited

def DFS_toposort(G):
    time = 0
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    toposort = []

    def DFS_visit(G, v):
        nonlocal time
        visited[v] = True
        time += 1
        for u in G[v]:
            if not visited[u]:
                parent[u] = v
                DFS_visit(G, u)
        time += 1
        toposort.append(v)

    for v in range(n):
        if not visited[v]: DFS_visit(G, v)

    return toposort

def critical(V, E):
    graph = to_adj(V, E)
    graph_modified = deepcopy(graph)
    visited_og = DFS_list(graph)
    visited_edge = None

    critical_cnt = 0

    for v in range(V):
        for u in graph[v]:
            graph_modified[v].remove(u)
            visited_edge = DFS_list(graph_modified)
            if visited_og != visited_edge: critical_cnt += 1
            graph_modified = deepcopy(graph)
    return critical_cnt

        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = False)

V = 4
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

print(critical(V, E))