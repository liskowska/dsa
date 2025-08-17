from copy import deepcopy

from egz1Atesty import runtests

def create_new_graph(G, V, r, t):
    base_graph = deepcopy(G)
    n = len(G)
    G.extend(deepcopy(base_graph))
    offset = 0

    for gold in V:
        offset += 1
        G[offset].append((offset*n+offset, gold))
        G[offset*n + t].append((t, 0))

        for v in range(n):
            for u, w in base_graph[v]:
                G[offset*n + v].append((offset*n + u , w*2 + r))
    return G

from queue import PriorityQueue

def dijkstra_list(G, s):
    n = len(G)

    d = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    queue = PriorityQueue()

    d[s] = 0
    queue.put((d[s], s))

    while not queue.empty():
        _d, v = queue.get()
        if not visited[v]:
            visited[v] = True
            for u, w in G[v]:
                if d[v] + w < d[u]: #relaksacja
                    d[u] = d[v] + w
                    parent[u] = v
                    queue.put((d[u], u))
    return d

def gold(G,V,s,t,r):
    new_graph = create_new_graph(G, V, r, t)
    distances = dijkstra_list(new_graph, s)
    return distances[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = False )

G = [[(1,9), (2,2)], # 0
[(0,9), (3,2), (4,6)], # 1
[(0,2), (3,7), (5,1)], # 2
[(1,2), (2,7), (4,2), (5,3)], # 3
[(1,6), (3,2), (6,1)], # 4
[(2,1), (3,3), (6,8)], # 5
[(4,1), (5,8)] ] # 6
V = [25,30,20,15,5,10,0]
s = 0
t = 6
r = 7

#print(create_new_graph(G, V, r, t))