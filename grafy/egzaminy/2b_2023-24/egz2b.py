"""
Złożoność O(ElogV) ~~ O(ElogE)???
Dijkstra na stanach
"""

from egz2btesty import runtests

def create_graph(E):
    n = 0
    for v, u, _w, _t in E:
        n = max(n, v, u)
    n+= 1
    graph = [[] for _ in range(n)]
    stan = -1

    for v, u, w, T in E:
        if T == 'I': stan = 0
        if T == 'P': stan = 1

        graph[v].append((u, w, stan))
        graph[u].append((v, w, stan))
    return graph

from queue import PriorityQueue
def dijkstra_tory(G, s, B):
    n = len(G)

    d = [[float('inf')]*2 for _ in range(n)]
    parent = [None for _ in range(n)]
    #visited = [False for _ in range(n)]
    queue = PriorityQueue()

    # 0 = I, 1 = P
    d[s][0] = 0
    d[s][1] = 0
    queue.put((0, s, 0))
    queue.put((0, s, 1))

    while not queue.empty():
        _d, v, stan_v = queue.get()

        for u, w, stan_u in G[v]:
            if v == s: w += 0 # startujemy
            elif stan_v == 0 and stan_u == 0: w += 5
            elif stan_v == 1 and stan_u == 1: w += 10
            else: w += 20

            if d[v][stan_v] + w < d[u][stan_u]: #relaksacja
                d[u][stan_u] = d[v][stan_v] + w
                parent[u] = v
                queue.put((d[u][stan_u], u, stan_u))
    return d[B]

def tory_amos( E, A, B ):
    graph = create_graph(E)
    ans = dijkstra_tory(graph, A, B)
    mini = float('inf')
    for i in ans:
        mini = min(mini, i)
    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )

G = [(0, 1, 5, 'P'), (1, 3, 1, 'I'), (3, 4, 1, 'I'),
 (2, 4, 1, 'P'), (2, 5, 1, 'I'), (0, 5, 5, 'P')]
A = 5
B = 3
