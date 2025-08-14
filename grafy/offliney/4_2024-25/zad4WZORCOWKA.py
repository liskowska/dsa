"""
złożoność: O(ElogV)
Najpierw tworzę listę sąsiedztwa z listy wierzchołków. Następnie dodaję jeden dodatkowy wierzchołek (o indekse n),
który połączony jest ze wszystkimi portalami krawędzią o wadze 0. Na nowym grafie G2 (w postaci listy sąsiedztwa)
puszczam dijkstre od wierzchołka a i zwracam distance[b] co jest równe najkrótszej trasie z wierzchołka a do
wierzchołka b.

złożoności funkcji:
to_list: O(E)
add_portals: O(|S|) == O(V)
dijkstra: O(ElogV)
___
spacetravel: O(ElogV)
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

def add_portals(graph, portals, n):
    graph.append([]) # dodaje wierzcholek, do ktorego beda dochodzily wszystkie portale
    for portal in portals:
        graph[n].append((0, portal))
        graph[portal].append((0, n))
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
    G2 = add_portals(G1, S, n)
    ans = dijkstra(G2, n + 1, a, b)
    if ans == float("inf"): return None
    else: return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
