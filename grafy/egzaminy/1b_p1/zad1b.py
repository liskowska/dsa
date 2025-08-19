from egzP1Btesty import runtests
"""
Zadanie polega na zaimplementowaniu algorytmu, ktory znajduje najkrotsza sciezke przechodzaca dokladnie przez
3 wierzcholki (nie licząc początkowego i końcowego).
Zadanie rażąco przypomina zadania 787 z leetcode, tylko tam ścieżka może przechodzić przez <= k wierzchołków,
a nie równo k wierzchołków.
"""
def turysta(G, D, L):

    def to_list(G):
        n = 0
        for v, u, w in G:
            n = max(v, u)
        n+=1

        adj_list = [[] for _ in range(n)]
        for u, v, w in G:
            adj_list[v].append((u, w))
            adj_list[u].append((v, w))

        return adj_list

    from queue import PriorityQueue
    def dijkstra_list_status(G, s, t, k):  # k - maximum stops that can be made
        n = len(G)

        d = [[float('inf')] * (k + 2) for _ in range(n)]
        parent = [None for _ in range(n)]
        queue = PriorityQueue()

        d[s][0] = 0
        queue.put((d[s][0], s, 0))  # odleglosc, wierzcholek, dlugosc krawedzi

        while not queue.empty():
            dist, v, st = queue.get()
            if st == k + 1: continue
            if dist > d[v][st]: continue
            for u, w in G[v]:
                new_dist = dist + w
                new_st = st + 1
                if new_dist < d[u][st + 1]:  # relaksacja
                    d[u][st + 1] = new_dist
                    parent[u] = v
                    queue.put((new_dist, u, new_st))
        return d[t][k]

    graph = to_list(G)
    ans = dijkstra_list_status(graph, D, L, 4)

    return ans

runtests(turysta)

G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
D = 0
L = 6