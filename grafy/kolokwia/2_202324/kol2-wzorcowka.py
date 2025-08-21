from kol2testy import runtests

def to_list(G):
    n = 0
    for v, u, _w in G:
        n = max(n, v, u)
    n += 1

    graph_list = [[] for _ in range(n)]
    for v, u, w in G:
        graph_list[v].append((u, w))
        graph_list[u].append((v, w))

    return graph_list

def graph_modify(G):
    for v in range(len(G)):
        G[v].append((v, 8))
    return G

from collections import deque
def BFS_status(G, s, status):
    n = len(G)
    Q = deque()
    parent = [None for _ in range(n)]
    distance = [[float("inf")]*17 for _ in range(n)]

    distance[s][16] = 0
    Q.append(s)

    while Q:
        v = Q.popleft()


    return

def warrior(G, s, t):
    g1 = to_list(G)
    graph = graph_modify(g1)

    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )