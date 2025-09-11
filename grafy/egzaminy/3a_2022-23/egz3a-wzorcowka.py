from collections import deque
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

    def bfs_modded(G, s):
        n = len(G)
        distance = [[float("inf") for _ in range(n)] for _ in range(17)]
        q = deque()
        distance[0][s] = 0
        q.append((s, 0, 0, 0)) # v, kroki do konca krawedzi, czas podrozy, dystans od s

        while q:
            u, step, tiredness, dist_u = q.popleft()
            if step > 0:
                q.append((u, step - 1, tiredness, dist_u))
                continue

            for v, w in G[u]:
                # rycerz nie ma siły
                if tiredness + w > 16:
                    new_tiredness = w
                    new_step = w + 8 # musimy przeczekac czas odpoczynku
                    new_dist = w + 8 + dist_u

                # rycerz ma sile i przechodzi przez wierzcholek v
                else:
                    new_tiredness = tiredness + w
                    new_step = w
                    new_dist = w + dist_u

                # sprawdzamy czy obecna ścieżka do v jest optymalna
                if distance[new_tiredness][v] > new_dist:
                    distance[new_tiredness][v] = new_dist
                    q.append((v, new_step - 1, new_tiredness, new_dist))

        return distance

    G_adj = to_adj(G)
    distance = bfs_modded(G_adj, s)

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