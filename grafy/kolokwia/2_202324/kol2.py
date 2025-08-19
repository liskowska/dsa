"""
Algorytm w złożoności podstawowej O(ElogV): Dijkstra ze stanami na zmodyfikowanym grafie z węzłami
"""
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


from queue import PriorityQueue
def dijkstra_status(G, s):
    n = len(G)
    d = [[float('inf')] * 17 for _ in range(n)]
    parent = [[None] * 17 for _ in range(n)]

    Q = PriorityQueue()
    d[s][16] = 0
    Q.put((0, s, 16))

    while not Q.empty():
        dist, v, status = Q.get()
        if dist > d[v][status]:
            continue

        # 1. relaksacja krawędzi
        for u, w in G[v]:
            if status - w < 0: continue
            cur_dist = dist + w
            cur_status = status - w
            if cur_dist < d[u][cur_status]:
                d[u][cur_status] = cur_dist
                parent[u][cur_status] = v
                Q.put((cur_dist, u, cur_status))

        # 2. reset w schronisku
        if dist + 8 < d[v][16]:
            d[v][16] = dist + 8
            Q.put((dist+8, v, 16))

    return d

def warrior(G, s, t):
    #tworze liste sasiedztwa grafu i dodaje do niego wezly o wartosci 8, odpowiadajace czasowi wypoczynku rycerza
    graph = to_list(G)
    graph = graph_modify(graph)

    n = len(graph)
    d = dijkstra_status(graph, s)
    print(d)
    mini = float("inf")
    for i in d[t]:
        mini = min(mini, i)
    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )

