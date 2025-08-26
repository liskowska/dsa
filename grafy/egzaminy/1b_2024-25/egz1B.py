from copy import deepcopy

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

def critical(V, E):
    graph = to_adj(V, E)
    graph_modified = deepcopy(graph)

    visited_og = None
    visited_new = None
    critical_cnt = 0

    for v in range(V):
        for u in graph[v]:
            graph_modified[v].remove(u)

            visited_og = BFS_list(graph, v)
            visited_new = BFS_list(graph_modified, v)

            if visited_og != visited_new: critical_cnt += 1
            graph_modified = deepcopy(graph)

    return critical_cnt

        
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(critical, all_tests = False)

V = 4
E = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

print(critical(5, [(1, 2), (3, 1), (4, 2), (3, 2), (1, 0), (3, 0)])) #4