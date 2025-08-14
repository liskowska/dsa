"""
Pomysł polega na stworzeniu listy sąsiedztwa następującego grafu:
  - na poczatek stworzenie grafu z wejścia funkcją to_list
 za pomoca funkcji add_bikes:
  - od kazdego wierzcholka w ktorym jest rower stworzyc krawedz jednostronna z waga zero, która prowadzi do
    kopii grafu wejściowego z wagami krawędzi pomnożonymi przez p/q
  - z kopii grafu z poprawioną wagą krawędzi, z wierzchołka odpowiadającemu wierzchołkowi t prowadzi krawędz jednostronna
    z wagą 0 do wierzchołka t
W taki sposób powstanie graf odpowiadający wszystkim możliwościom odbycia maratonu. Następnie puszczam przez
powstały graf algorytm Dijkstry od wierzchołka s, a distance[t] zwróci mi odpowiedź do zadania i pani
Silnoręka będzie miała dużą szansę na wygranie maratonu. #girlpower
"""
from copy import deepcopy
from queue import PriorityQueue

from egz1atesty import runtests


def to_list(edges, n):
  graph = [[] for _ in range(n)]
  for v, u, w in edges:
    graph[v].append((w, u))
    graph[u].append((w, v))
  return graph

def add_bikes(graph, B, t):
    base_graph = deepcopy(graph)
    n = len(graph)
    bikes_cnt = 0
    for i, p, q in B:
        scaler = float(p / q)
        if scaler > 1: continue

        bikes_cnt += 1
        graph.extend(deepcopy(base_graph))

        graph[i].append((0, bikes_cnt*n + i))
        graph[ bikes_cnt*n + t].append((0, t))

        for v in range(bikes_cnt+n, len(graph)):
            for w, u in graph[v]:
                w *= scaler
    return graph

from math import floor
def dijkstra(G, s, k):
    n = len(G)
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
                    distance[u] = floor(distance[v] + w)
                    parent[u] = v
                    Q.put((distance[u], u))
    return distance[k]


def armstrong( B, G, s, t):
    n = len(G)
    base_graph = to_list(G, n)
    graph = add_bikes(base_graph, B, t)
    ans = dijkstra(graph, s, t)
    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = False )

B = [ (1, 1, 2), (2, 2, 3) ]
G = [ (0,1,6), (1,4,7), (4,3,4),
 (3,2,4), (2,0,3), (0,3,6) ]
s = 0
t = 4

graph1  = to_list(G, 5)
farmazon = add_bikes(graph1, B, t)
print(armstrong(B, G, s, t))
