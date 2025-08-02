from turtledemo.clock import current_day

from dsa.grafy.algorytmy_podstawowe.BFS import shortest_path
from zad3testy import runtests
"""
Algorytm w złożoności akceptowalnej O(VE+E^2) polega na usuwaniu każdej krawędzi po kolei i sprawdzanie BFSem, czy
wydłuża to ścieżkę od s do t.
Algorytm i jego wytłumaczenie w wersji wzorcowej znajduje się poniżej.
"""

#O(VE+E^2)
from collections import deque
from copy import deepcopy
def longer( G, s, t ):

    def BFS_list(G, s, t):
        n = len(G)
        Q = deque()

        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        d = [float('inf') for _ in range(n)]

        d[s] = 0
        visited[s] = True
        Q.append(s)

        while Q:
            u = Q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    d[v] = d[u] + 1
                    Q.append(v)

        return d[t]

    d = BFS_list(G, s, t)
    for v in range(len(G)):
        for u in G[v]:
            new_graph = deepcopy(G)
            new_graph[v].remove(u)
            new_graph[u].remove(v)
            new_d = BFS_list(new_graph, s, t)
            if new_d != d: return v, u

    return None

#O(V+E)
def longer2(G, s, t):
    def BFS_list(G, s):
        n = len(G)
        Q = deque()

        visited = [False for _ in range(n)]
        parent = [None for _ in range(n)]
        d = [float('inf') for _ in range(n)]

        d[s] = 0
        visited[s] = True
        Q.append(s)

        while Q:
            u = Q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    d[v] = d[u] + 1
                    Q.append(v)

        return d, parent

    d, parent = BFS_list(G, s)
    def createBFS_DAG(G, d):
        n = len(G)
        parent_dag = [[] for _ in range(n)]
        G_dag = [[] for _ in range(n)]
        for u in range(n):
            for v in G[u]:
                if d[v] == d[u] + 1:
                    G_dag[u].append(v)
                    parent_dag[v].append(u)
        return G_dag, parent_dag

    G_dag, parent_dag = createBFS_DAG(G, d)
    def paths_maker(parent, s, t):
        if t == s: return [[s]]
        if len(parent[t]) == 0: return []
        paths = []
        for p in parent[t]:
            for path in paths_maker(parent, s, p):
                paths.append(path + [t])
        return paths

    paths = paths_maker(parent_dag, s, t)
    def shortest_paths_maker(paths):
        shortest_paths = []
        cnt = 0
        cur_cnt = 0
        for path in paths:
            for i in path: cur_cnt += 1
            if cur_cnt < cnt: cnt = cur_cnt
            cur_cnt = 0

    return paths[0][0], paths[0][1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer2, all_tests = True )
