"""
Myślałam że mogę zaimplementować wzorcówkę zaczynając od n-1 najmniejszej krawędzi (bo w mst jest
n-1 krawedzi) a nastepnie isc w coraz mniejsze krawedzie dopoki nie znajde cyklu (albo stworze drzewo)
a pozniej w coraz wieksze krawedzie dopoki nie powstanie drzewo. Niestety to nie działa
(kontrprzykladem jest test 1.) ale poswiecilam na te implementacje duzo za duzo czasu zeby to teraz usunac.
Zostawiam wiec dla przestrogi.
"""

from kol2testy import runtests

def to_edges(G):
    edges = []
    n = len(G)
    for v in range(n):
        for u, w in G[v]:
            if v > u: continue
            edges.append((v, u, w))
    return edges, n



def create_beautree(E, n):
    parent = [_ for _ in range(n)]
    rank = [1 for _ in range(n)]
    def Find(parent, x):
        if parent[x] != x:
            parent[x] = Find(parent, parent[x])
        return parent[x]

    def Union(parent, rank, x, y):
        x = Find(parent, x)
        y = Find(parent, y)
        if x == y:
            return False

        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1
        return True

    m = len(E)

    starting_edge = n-2
    cur_edge = starting_edge
    status = 'down'
    tree_weight = 0
    taken = 0
    z = None

    while taken < n -1:
        z = Union(parent, rank, E[cur_edge][0], E[cur_edge][1])
        if z:
            tree_weight += E[cur_edge][2]
            taken += 1
            if status == 'down':
                cur_edge -= 1
                if cur_edge < 0:
                    status = 'up'
                    cur_edge = starting_edge + 1
            elif status == 'up':
                cur_edge += 1
                if cur_edge >= m: return None
        elif not z:
            if status == 'up': return None
            elif status == 'down':
                status = 'up'
                cur_edge = starting_edge + 1
    return tree_weight


def beautree(G):
    E, n = to_edges(G)
    E.sort(key=lambda x:x[2])
    return create_beautree(E, n)

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests(beautree, all_tests=True)

G1 = [ [(1,3), (2,1), (4,2)], # 0
[(0,3), (2,5) ], # 1
[(1,5), (0,1), (3,6)], # 2
[(2,6), (4,4) ], # 3
[(3,4), (0,2) ] ] # 4

G2 = [ [(1,2), (2,3)], # 0
        [(0,2), (2,1), (3,5), (4,6)], # 1
        [(0,3), (1,1), (3,9), (4,4)], # 2
        [(1,5), (2,9), (4,10), (5,8)], # 3
        [(2,4), (1,6), (3,10), (5,7)], # 4
        [(3,8), (4,7)] ] # 5

print(beautree(G2))
