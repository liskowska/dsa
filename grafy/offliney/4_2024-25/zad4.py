"""
złożoność lepsza: O(V^2 + ElogV)
"""
from queue import PriorityQueue
from zad4testy import runtests

# (w, v) --> waga, wierzcholek
def to_list(edges, n):
    graph = [[] for _ in range(n)]
    for v, u, w in edges:
        graph[v].append((w, u))
        graph[u].append((w, v))
    return graph

def add_portals(graph, portals):
    for i in range(len(portals)):
        portal1 = portals[i]
        for j in range(i+1, len(portals)):
            portal2 = portals[j]

            graph[portal1].append((0, portal2))
            graph[portal2].append((0, portal1))

    return graph

def dijkstra(G, n, s, k):
    distance = [float("inf") for _ in range(n)]
    parent = [None for _ in range(n)]
    visited = [None for _ in range(n)]
    Q = PriorityQueue()

    distance[s] = 0
    Q.put((0, s))

    while not Q.empty():
        _dist, v = Q.get()
        if not visited[v]:
            visited[v] = True
            #relaksacja
            for w, u in G[v]:
                if  distance[v] + w < distance[u]:
                    distance[u] = distance[v] + w
                    parent[u] = v
                    Q.put((distance[u], u))
    return distance[k]

def spacetravel( n, E, S, a, b ):
    G1 = to_list(E, n)
    G2 = add_portals(G1, S)
    ans = dijkstra(G2, n, a, b)
    if ans == float("inf"): return None
    else: return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
