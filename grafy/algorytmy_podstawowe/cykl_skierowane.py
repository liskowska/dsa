"""
==> szukanie cyklu w niespójnym grafie skierowanym
    - jest cykl -> return False
    - nie ma cyklu -> return True

żeby graf skierowany miał cykl, przechodząc przez graf dfs-em, wierzchołek musi być odwiedzony ponownie podczas
tej samej "wędrówki"
"""


def isCycle(n, G):
    visited = [False for _ in range(n)]
    cur_visited = [False for _ in range(n)]

    def dfsCycle(G, v):
        def dfsVisit(G, v):
            visited[v] = True
            cur_visited[v] = True

            for u in G[v]:
                if cur_visited[u]: return True
                if not visited[u]:
                    if dfsVisit(G, u): return True

            cur_visited[v] = False
            return False

        for u in G[v]:
            if not visited[u]:
                if dfsVisit(G, u): return True
        return False

    for v in range(n):
        for u in G[v]:
            if not visited[u]:
                if dfsCycle(G, u) is True: return False
    return True