from math import inf

def Find(parent, x):
    if parent[x] != x:
        parent[x] = Find(parent, parent[x])
    return parent[x]


def Union(parent, rank, x, y):
    x = Find(parent, x)
    y = Find(parent, y)
    if x == y:
        return

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


def Kruskal_list(G):
    parent = [_ for _ in range(len(G))]
    rank = [1 for _ in range(len(G))]
    edges = []
    MST = []
    taken = 0

    for v in range(len(G)):
        for u, weight in G[v]:
            edges.append((v, u, weight))
    edges = sorted(edges, key=lambda item: item[2])

    for edge in edges:
        if taken == len(G) - 1:
            return MST
        x = Find(parent, edge[0])
        y = Find(parent, edge[1])

        if x != y:
            Union(parent, rank, x, y)
            taken += 1
            MST.append(edge)
    print("Something went wrong!")


def Kruskal_matrix(G):
    parent = [_ for _ in range(len(G))]
    rank = [1 for _ in range(len(G))]
    edges = []
    MST = []
    taken = 0

    for u, edge in enumerate(G):
        for v, weight in enumerate(edge):
            if weight != inf and u < v:
                edges.append((u, v, weight))
    edges.sort(key=lambda item: item[2])

    for edge in edges:
        if taken == len(G) - 1:
            return MST
        x = Find(parent, edge[0])
        y = Find(parent, edge[1])

        if x != y:
            Union(parent, rank, x, y)
            taken += 1
            MST.append(edge)
    print("Something went wrong!")