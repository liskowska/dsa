"""
O(nlogm)
"""

from egzP3btesty import runtests
from queue import PriorityQueue

def lufthansa ( G ):
    n = len(G)
    parent = [-1 for _ in range(n + 1)]

    # zwraca parent/root/set do ktorego nalezy wierzcholek
    def find(v):
        if parent[v] < 0:
            return v
        parent[v] = find(parent[v])  # path compression
        return parent[v]

    # False: dodanie v tworzy cykl (nie dodalismy krawedzi)
    # True: dodanie nie v stworzy cyklu (dodalismy krawedz)
    def union(v, u):
        rootv, rootu = find(v), find(u)
        if rootv == rootu:
            return False  # union v i u stworzyłby cykl
        else: #dopinamy do wiekszego roota
            rank = parent[rootv] + parent[rootu]
            if parent[rootv] > parent[rootu]: # rootu jest wiekszy
                parent[rootv] = rootu
                parent[rootu] = rank
            else:
                parent[rootu] = rootv
                parent[rootv] = rank
            return True

    def to_edges(G):
        edges = []
        total_w = 0
        for v in range(len(G)):
            for u, w in G[v]:
                if u < v: continue
                edges.append((v, u, w))
                total_w += w
        return edges, total_w


    #Tworzenie kolejki priorytetowej z priorytetem dla wag
    queue = PriorityQueue()
    edges, total_w = to_edges(G)
    for v, u, w in edges: #nlogm
        neg_w = -w
        queue.put((neg_w, v, u)) #-w, zeby ustawily mi sie w kolejce od najwiekszego

    ans = 0
    use = 0
    while not queue.empty():
        neg_w, v, u = queue.get() #logm
        w = -neg_w
        if union(v, u):
            ans += w
        else:
            if use == 0:
                use += 1
                ans += w
    # for v1, v2 in G:
    #     if not union(v1, v2): return [v1, v2]
    return total_w - ans

runtests(lufthansa, all_tests=True)