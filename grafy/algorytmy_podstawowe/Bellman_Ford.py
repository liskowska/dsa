"""
działa dla wag ujemnych
wejście: graf skierowany
złożoność czasowa: O(VE)
"""

from math import inf

def Edges(G):
    for index, neighbours in enumerate(G):
        for destination, weight in neighbours:
            yield index, destination, weight


# O( V * E )
def bellman_ford(G, s):
    distance = [inf for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    distance[s] = 0

    edges = 0
    for i in range(len(G)):
        edges += len(G[i])

    for i in range(len(G) - 1):
        #        for index, neighbours in enumerate(G):
        #            for u, weight in neighbours:
        for i in range(edges):
            for v, u, weight in Edges(G):
                if distance[v] != inf and distance[u] > distance[v] + weight:
                    distance[u] = distance[v] + weight
                    parent[u] = v

    for i in range(edges):
        for v, u, weight in Edges(G):
            if distance[v] != inf and distance[u] > distance[v] + weight:
                print("negative weight cycle")
                return

    print("distance from ", s, ": ")
    print(distance)
    print("parents: ")
    print(parent)


G = [[(1, 6), (2, 5), (3, 5)],
     [(4, -1)],
     [(1, -2), (4, 1)],
     [(2, -2), (5, -1)],
     [(6, 3)],
     [(6, 3)],
     []]
bellman_ford(G, 0)
# Graf ważony skierowany - lista sąsiedztwa
# Indeksy wierzchołków: 0, 1, 2, 3, 4

G = [
    [(1, 6), (2, 7)],        # wierzchołek 0: krawędzie 0→1 (waga 6), 0→2 (waga 7)
    [(2, 8), (3, 5), (4, -4)],  # wierzchołek 1: 1→2 (8), 1→3 (5), 1→4 (-4)
    [(3, -3), (4, 9)],       # wierzchołek 2: 2→3 (-3), 2→4 (9)
    [(1, -2)],               # wierzchołek 3: 3→1 (-2)
    [(0, 2), (3, 7)]         # wierzchołek 4: 4→0 (2), 4→3 (7)
]

print(bellman_ford(G, 0))
