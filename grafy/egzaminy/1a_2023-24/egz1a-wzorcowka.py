"""
Pomysł polega na poprowadzeniu dwa razy algortymu dijkstry: od a do b (D1) oraz od b do a (D2) i zapamietanie ich tablic
distance. Następnie przechodzę przez tablicę B i obliczam koszt przejscia z kazdym rowerem w sposob nastepujacy:
koszt przejscia = koszt dojscia do roweru z a + [(koszt dojscia do roweru z b) * p/q]
inaczej:
x = D[i] + D2[i]*(p/q)
Na bieżąco aktualizuję zmienną mini, gdzie znajduje się najniższy możliwy czas przebycia maratonu.
"""

from egz1atesty import runtests

#(w, v) - waga, sasiad
def to_list(edges):
    n = 0
    for v, u, w in edges:
        n = max(n, v, u)
    n += 1

    graph = [[] for _ in range(n)]
    for v, u, w in edges:
        graph[v].append((w, u))
        graph[u].append((w, v))
    return graph

from queue import PriorityQueue
def dijkstra(G, s):
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
                    distance[u] = distance[v] + w
                    parent[u] = v
                    Q.put((distance[u], u))
    return distance

def armstrong(B, G, s, t):
    graph = to_list(G)
    D1 = dijkstra(graph, s)
    D2 = dijkstra(graph, t)

    mini = D1[t] # wartosc przejscia calej drogi pieszo
    for i, p, q in B:
        mini = min(mini,  D1[i] + (D2[i] * p/q))
    mini = int(mini)
    return mini

runtests( armstrong, all_tests = True )

B = [ (1, 1, 2), (2, 2, 3) ]
G = [ (0,1,6), (1,4,7), (4,3,4),
 (3,2,4), (2,0,3), (0,3,6) ]
s = 0
t = 4
