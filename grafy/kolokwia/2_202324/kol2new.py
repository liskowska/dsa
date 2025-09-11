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

from queue import PriorityQueue
def dijkstra(G, s):
    n = len(G)
    distance = [[float("inf") for _ in range(n)] for _ in range(17)]
    Q = PriorityQueue()

    distance[0][s] = 0
    Q.put((0, s, 0)) #dist, v, tiredness

    while not Q.empty():
        dist, u, tiredness = Q.get()
        if dist > distance[tiredness][u]: continue
        for v, w in G[u]:
            if (tiredness + w <= 16) and (distance[tiredness][u] + w < distance[tiredness + w][v]):
                distance[tiredness + w][v] = distance[tiredness][u] + w
                Q.put((distance[tiredness + w][v], v, tiredness + w))

        if dist + 8 < distance[0][u]:
            distance[0][u] = dist + 8
            Q.put((dist, u, 0))

    return distance

def warrior(G, s, t):
    graph = to_list(G)

    n = len(graph)
    d = dijkstra(graph, s)
    print(d)
    mini = float("inf")
    for i in range(17):
        mini = min(mini, d[i][t])
    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )