from egz1Atesty import runtests

def build_layered_graph(G, V, r):
    n = len(G)
    new_G = [[] for _ in range(2*n)]

    for v in range(n):
        # 1. zwykłe krawędzie (warstwa 0)
        for u, w in G[v]:
            new_G[v].append((u, w))           # (v,0) -> (u,0)
            new_G[n+v].append((n+u, 2*w + r)) # (v,1) -> (u,1)

        # 2. opcja rabunku
        new_G[v].append((n+v, -V[v]))         # (v,0) -> (v,1)

    #print(new_G)
    return new_G

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
    new_graph = build_layered_graph(G, V, r)
    n = len(G)
    distances = dijkstra_list(new_graph, s)
    return min(distances[t], distances[t+n])

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