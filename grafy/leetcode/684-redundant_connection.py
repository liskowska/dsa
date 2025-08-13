"""
684. Redundant Connection
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed.
The graph is represented as an array edges of length n where edges[i] = [a, b] indicates that there is an edge
between nodes a and b in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes.
If there are multiple answers, return the answer that occurs last in the input.
"""

# beats 100% on leetcode!!! B) :fire::fire:

"""
Znajduje cykl za pomocą struktury find-union. Moje find-union zbudowane jest na jednej tablicy parent, gdzie:
- parent[v] = u, u>0 ==> u jest rodzicem v
- parent[v] = x, x<0 ==> v jest "rootem", a -x jest rangą, czyli liczbą wierzchołków (łącznie z v), które podlegają pod
  root v
"""

def findRedundantConnection(edges):
    n = len(edges)
    parent = [-1 for _ in range(n + 1)]

    # zwraca parent/root/set do ktorego nalezy wierzcholek
    def find(v):
        par = parent[v]
        prev_par = v
        while par > 0:
            prev_par = par      # zapamietuje poprzedniego parenta, zeby nie zwrocic rangi/"parenta" roota tylko roota
            par = parent[par]
        return prev_par

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

    for edge in edges:
        v1, v2 = edge[0], edge[1]
        if not union(v1, v2): return [v1, v2]
    return -1

# output: [2, 3]
edges1 = [[1,2],[1,3],[2,3]]
print(findRedundantConnection(edges1))

# output: [1, 4]
edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
print(findRedundantConnection(edges2))