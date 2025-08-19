from zad3testy import runtests

from collections import deque
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

    return d

from math import inf

Time = 0
def Bridges_util(G, visited, parent, time, low, v):
    global Time
    visited[v] = True
    time[v] = Time
    low[v] = Time
    Time += 1

    for u in G[v]:
        if not visited[u]:
            parent[u] = v

            Bridges_util(G, visited, parent, time, low, u)
            low[v] = min(low[u], low[v])

        elif u != parent[v]:
            low[v] = min(low[v], time[u])

def Bridges_list(G):
    visited = [False for _ in range(len(G))]
    parent = [None for _ in range(len(G))]
    time = [inf for _ in range(len(G))]
    low = [inf for _ in range(len(G))]
    bridges = []

    for i in range(len(G)):
        if not visited[i]:
            Bridges_util(G, visited, parent, time, low, i)

    for i in range(len(G)):
        if parent[i] is not None and time[i] == low[i]:
            bridges.append((i, parent[i]))

    return bridges

def longer( G, s, t ):
    n = len(G)
    dist_s = BFS_list(G, s)
    dist_t = BFS_list(G, t)
    shortest_path = dist_s[t]

    # tworzenie grafu najkrótszych ścieżek
    new_graph = [[] for _ in range(n)]
    for v in range(n):
        for u in G[v]:
            if dist_s[v] + dist_t[u] + 1 == shortest_path or dist_t[u] + dist_s[v] + 1 == shortest_path:
                new_graph[v].append(u)
                new_graph[u].append(v)
    # new_graph został grafem najkrótszych ścieżek z s do t

    bridge = Bridges_list(new_graph)
    if not bridge: return None
    else: return bridge[0]


runtests( longer, all_tests = True )