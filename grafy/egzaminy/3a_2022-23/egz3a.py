from queue import PriorityQueue
from egz3atesty import runtests

def goodknight( G, s, t ):
    def to_adj(G):
        n = len(G)
        G_adj = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                if G[i][j] != -1:
                    G_adj[i].append((j, G[i][j]))
                    G_adj[j].append((i, G[i][j]))
        return G_adj

    def dijkstra(G, s):
        n = len(G)
        distance = [[float("inf") for _ in range(n)] for _ in range(17)]

        Q = PriorityQueue()
        distance[0][s] = 0
        Q.put((0, s, 0))

        while not Q.empty():
            dist_u, u, tiredness = Q.get()
            if dist_u > distance[tiredness][u]: continue
            for v, w in G[u]:
                if tiredness + w <= 16:
                    if distance[tiredness][u] + w < distance[tiredness + w][v]:
                        distance[tiredness + w][v] = distance[tiredness][u] + w
                        Q.put(( distance[tiredness + w][v], v, tiredness + w))

            if dist_u + 8 < distance[0][u]:
                distance[0][u] = dist_u + 8
                Q.put((distance[0][u], u, 0))
        return distance

    G_adj = to_adj(G)
    distance = dijkstra(G_adj, s)

    res = float("inf")
    for i in range(len(distance)):
        if distance[i][t] < res: res = distance[i][t]

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True )

# G = [ \
# [ -1, 3, 8,-1,-1,-1 ], # 0
# [ 3,-1, 3, 6,-1,-1 ], # 1
# [ 8, 3,-1,-1, 5,-1 ], # 2
# [ -1, 6,-1,-1, 7, 8 ], # 3
# [ -1,-1, 5, 7,-1, 8 ], # 4
# [ -1,-1,-1, 8, 8,-1 ]] # 5
# s = 0
# t = 5
#
# print(goodknight(G, s, t))
